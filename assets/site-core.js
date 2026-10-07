/*
  Site Core v2 — dependency-free shared helpers.
  Existing page scripts remain untouched for backwards compatibility.
*/
(function () {
  "use strict";

  var core = {
    version: "2.0.0",
    ready: function (fn) {
      if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", fn, { once: true });
      } else {
        fn();
      }
    },
    one: function (selector, root) {
      return (root || document).querySelector(selector);
    },
    all: function (selector, root) {
      return Array.prototype.slice.call((root || document).querySelectorAll(selector));
    }
  };

  window.SiteCore = window.SiteCore || core;
})();
