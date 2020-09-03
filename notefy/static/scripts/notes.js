(function ($) {
  // Not original function that returns query string as some kind of dict
  function getUrlVars() {
    var vars = [],
      hash;
    var hashes = window.location.href
      .slice(window.location.href.indexOf("?") + 1)
      .split("&");
    for (var i = 0; i < hashes.length; i++) {
      hash = hashes[i].split("=");
      vars.push(hash[0]);
      vars[hash[0]] = hash[1];
    }
    return vars;
  }

  if (typeof getUrlVars()["subject"] == "undefined") {
    $(".notes-nav").find("li").first().addClass("notes-nav-selected");
  } else {
    $(".notes-nav").find($("li[subject=" + getUrlVars()["subject"] + "]")).addClass(
      "notes-nav-selected"
    );
  }

  $(".notes-nav")
    .find("li")
    .on("click", function () {
      var target_url;
      if ($(this).attr("subject") == "none") {
        target_url = window.location.pathname;
      } else {
        target_url =
          window.location.pathname + "?subject=" + $(this).attr("subject");
      }
      window.location.replace(target_url);
    });

  $(".my-notes").on("click", function () {
    window.location.replace(window.location.href + "&folder=my-notes");
  });
  $(".favorite").on("click", function () {
    window.location.replace(window.location.href + "&folder=favorite");
  });
  $(".mistake-collection").on("click", function () {
    window.location.replace(
      window.location.href + "&folder=mistake-collection"
    );
  });

  $("#subject_arrow").on("click", function (e) {
    $("#subject_box").toggle();
    e.stopPropagation();
  });

  $(".upload-block").on("click", function () {
    $(".upload").show()
  });

  $(document).on('click', function (e) {
    if ($(e.target).closest(".drop-down-box").length === 0) {
        $(".drop-down-box").hide();
    }
  });
})(jQuery);
