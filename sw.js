// Offline support, faster start-up + phone notifications.
const CACHE = "neartask-v11";
self.addEventListener("install", (e) => {
  e.waitUntil(caches.open(CACHE).then((c) => c.addAll(["./", "./index.html", "./icon.svg", "./apple-touch-icon.png", "./icon-192.png", "./manifest.webmanifest"])).catch(() => {}));
  self.skipWaiting();
});
self.addEventListener("activate", (e) => {
  e.waitUntil(caches.keys().then((keys) => Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k)))));
  self.clients.claim();
});

function save(req, res) {
  if (res && (res.ok || res.type === "opaque")) {
    const copy = res.clone();
    caches.open(CACHE).then((c) => c.put(req, copy)).catch(() => {});
  }
  return res;
}

self.addEventListener("fetch", (e) => {
  const req = e.request;
  if (req.method !== "GET") return;
  const url = new URL(req.url);

  // Libraries with a fixed version number (the database library from jsDelivr) and Google font files never change:
  // keep them on the phone so the app does not download them again on every start.
  const fixedLibrary = url.hostname === "cdn.jsdelivr.net" && /@\d/.test(url.pathname);
  if (fixedLibrary || url.hostname === "fonts.gstatic.com") {
    e.respondWith(caches.match(req).then((hit) => hit || fetch(req).then((res) => save(req, res))));
    return;
  }
  if (url.origin !== self.location.origin) return;

  // Opening the app: start from the saved copy straight away (no waiting for the network) and fetch the newest
  // version in the background, so it is used the next time the app opens. Without a saved copy, wait for the network.
  if (req.mode === "navigate") {
    const net = fetch(req).then((res) => save(req, res));
    e.respondWith(
      caches.match(req).then((r) => r || caches.match("./index.html"))
        .then((r) => r || net)
        .catch(() => net)
    );
    e.waitUntil(net.catch(() => {}));
    return;
  }

  e.respondWith(
    fetch(req)
      .then((res) => save(req, res))
      .catch(() => caches.match(req).then((r) => r || caches.match("./index.html")))
  );
});
self.addEventListener("push", (e) => {
  let d = {};
  try { d = e.data ? e.data.json() : {}; } catch {}
  e.waitUntil(self.registration.showNotification(d.title || "NearTask", { body: d.body || "", icon: "icon.svg", badge: "icon.svg", tag: d.id || undefined, data: { link: d.link || "/" } }));
});
self.addEventListener("notificationclick", (e) => {
  e.notification.close();
  const url = self.registration.scope + "#" + ((e.notification.data && e.notification.data.link) || "/");
  e.waitUntil(self.clients.matchAll({ type: "window" }).then((cs) => {
    for (const c of cs) if ("focus" in c) { c.navigate(url); return c.focus(); }
    return self.clients.openWindow(url);
  }));
});
