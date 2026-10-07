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

  // Health Assistant loader: isolated from page-specific scripts.
  // If either asset fails to load, the page itself continues normally.
  core.ready(function () {
    if (document.querySelector('script[data-ieai-loader]')) return;

    var cssHref = "/assets/health-assistant.css";
    if (!document.querySelector('link[href="' + cssHref + '"]')) {
      var link = document.createElement("link");
      link.rel = "stylesheet";
      link.href = cssHref;
      link.setAttribute("data-ieai-loader", "css");
      document.head.appendChild(link);
    }

    var script = document.createElement("script");
    script.src = "/assets/health-assistant.js";
    script.defer = true;
    script.setAttribute("data-ieai-loader", "js");
    document.head.appendChild(script);
  });
})();
