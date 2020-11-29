var CACHE_NAME = 'my-site-cache-v1';
var urlsToCache = [
    '/',
    '/galeria/',
    '/static/css/style.css',
    '/static/img/logo.png',
];

self.addEventListener('install', function(event) {
  // Perform install steps
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
});

self.addEventListener('fetch', function(event) {
    event.respondWith(
        caches.match(event.request).then(function(response) {

          return fetch(event.request)
          .catch(function(rsp) {
             return response; 
          });
          
          
        })
    );
});

/////////////////////////////////////////////////////////////////////
importScripts('https://www.gstatic.com/firebasejs/8.1.1/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/8.1.1/firebase-messaging.js');

// Your web app's Firebase configuration
var firebaseConfig = {
  apiKey: "AIzaSyDpzcnW1kMRlvTr9Sqj2pKW9337Wi_5K5Y",
  authDomain: "project-cleancar.firebaseapp.com",
  databaseURL: "https://project-cleancar.firebaseio.com",
  projectId: "project-cleancar",
  storageBucket: "project-cleancar.appspot.com",
  messagingSenderId: "866705797907",
  appId: "1:866705797907:web:4ff2b9a648fb139b3260e6"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);
/////////////////////////////////////////////////////////////////////
let messaging = firebase.messaging()

// generar el modelo de envío de notificaciones por Firebase
messaging.setBackgroundMessageHandler(function(payload) {
  let titulo = payload.notification.title
  let opciones = {
      body: payload.notification.body,
      icon: payload.notification.icon
  }
  self.registration.showNotification(titulo, opciones)
})
