(function ($) {
  var queryString = new URLSearchParams(window.location.search);

  if (!queryString.has("subject")) {
    $(".notes-nav").find("li").first().addClass("notes-nav-selected");
  } else {
    $(".notes-nav")
      .find($("li[subject=" + queryString.get("subject") + "]"))
      .addClass("notes-nav-selected");
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

  $(".drop-down-arrow").on("click", function (e) {
    $(this).prev().toggle();
    e.stopPropagation();
  });

  $(".upload-block").on("click", function (e) {
    $(".upload").show();
  });

  $(document).on("click", function (e) {
    if ($(e.target).closest(".drop-down-box").length === 0) {
      $(".drop-down-box").hide();
    }
    if (
      $(e.target).closest(".upload").length === 0 &&
      $(".upload-overlay").css("display") == "flex"
    ) {
      $(".upload-overlay").hide();
    }
    if ($(e.target).closest(".note-management-box").length === 0) {
      $(".note-management-box").hide();
    }
  });

  $("#note_file").on("change", function () {
    var file = $(this).prop("files")[0];
    if (file.size > 10485760) {
      alert("File size can not exceed 10mb");
      this.value = "";
    }
  });

  $(".upload-block").on("click", function (e) {
    $(".upload-overlay").show().css("display", "flex");
    e.stopPropagation();
  });

  $("#submit_note").on("click", function () {
    var topics = [];
    $(".topics-container").each(function () {
      if ($(this).find("input").is(":checked")) {
        topics.push($(this).find("input").attr("id"));
      }
    });
    var file = $("#note_file").prop("files")[0];
    var reader = new FileReader();
    reader.readAsDataURL(file);
    data = new FormData();
    data.append("file", file);
    data.append("topics", topics);
    data.append("subject", queryString.get("subject"));
    $.ajax({
      type: "POST",
      url: "/upload_notes",
      data: data,
      cache: false,
      contentType: false,
      processData: false,
      success: function (response) {
        $(".upload-overlay").hide();
        switch (response.code) {
          case 0:
            alert("Upload Success");
            break;
          case 1:
            alert("Invalid Subject");
            break;
          case 2:
            alert("Invalid Topic");
            break;
          case 3:
            alert("Bad file upload");
            break;
          case 4:
            alert("File extension is not allowed");
            break;
        }
      },
    });
  });

  function changeDisplayNumber(element, value) {
    element.text(parseInt(element.text()) + value);
  }

  var hover;
  $(".action-like").hover(
    function () {
      if ($(this).attr("src") == "/static/images/icons/red-heart-empty.svg") {
        $(this).attr("src", "/static/images/icons/red-heart.svg");
        hover = true;
      } else {
        hover = false;
      }
    },
    function () {
      if (hover) {
        $(this).attr("src", "/static/images/icons/red-heart-empty.svg");
      }
    }
  );
  $(".action-favorite").hover(
    function () {
      if ($(this).attr("src") == "/static/images/icons/favorite-empty.svg") {
        $(this).attr("src", "/static/images/icons/favorite.svg");
        hover = true;
      } else {
        hover = false;
      }
    },
    function () {
      if (hover) {
        $(this).attr("src", "/static/images/icons/favorite-empty.svg");
      }
    }
  );

  $(".action-like, .action-favorite").on("click", function (e) {
    e.stopPropagation();
    var $note_block = $(this).parents(".note-block");
    var note_id = $note_block.attr("id");
    var data = new FormData();
    if ($(this).hasClass("action-like")) {
      var action = "like";
    } else {
      var action = "favorite";
    }
    data.append("note_id", note_id);
    data.append("action", action);
    $.ajax({
      type: "POST",
      url: "/handle_note_action",
      data: data,
      cache: false,
      contentType: false,
      processData: false,
      success: function (response) {
        switch (response.message) {
          case "liked":
            changeDisplayNumber($note_block.find(".note-likes"), 1);
            $note_block
              .find(".action-like")
              .attr("src", "/static/images/icons/red-heart.svg");
            hover = false;
            break;
          case "un-liked":
            changeDisplayNumber($note_block.find(".note-likes"), -1);
            $note_block
              .find(".action-like")
              .attr("src", "/static/images/icons/red-heart-empty.svg");
            break;
          case "favorite":
            changeDisplayNumber($note_block.find(".note-favorites"), 1);
            $note_block
              .find(".action-favorite")
              .attr("src", "/static/images/icons/favorite.svg");
            hover = false;
            break;
          case "un-favorite":
            changeDisplayNumber($note_block.find(".note-favorites"), -1);
            $note_block
              .find(".action-favorite")
              .attr("src", "/static/images/icons/favorite-empty.svg");
            break;
        }
      },
    });
  });

  $(".drop-down-box")
    .find("li")
    .on("click", function () {
      var $dropDownBox = $(this).parents(".drop-down-box");
      if ($dropDownBox.attr("id") == "topic_box") {
        queryString.delete("topic_filter");
        queryString.append("topic_filter", $(this).text());
      } else if ($dropDownBox.attr("id") == "subject_box") {
        queryString.delete("subject_filter");
        queryString.append("subject_filter", $(this).attr("subject"));
      }
      window.location.replace(
        window.location.pathname + "?" + queryString.toString()
      );
    });

  if (queryString.has("topic_filter")) {
    $("#topic_box").prev().text(queryString.get("topic_filter"));
  }

  if (queryString.has("subject_filter")) {
    var text = $("li[subject='" + queryString.get("subject_filter") + "']")
      .first()
      .text();
    $("#subject_box").prev().text(text);
  }

  $(".note-block").on("click", function () {
    if (!$(this).hasClass("upload-block")) {
      window.open("/download_note" + "?" + "note_id=" + $(this).attr("id"));
    }
  });

  $(".note-management").on("click", function (e) {
    e.stopPropagation();
    $(this).next().toggle();
  });

  $(".note-management-box")
    .find("li")
    .first()
    .on("click", function (e) {
      var note_id = $(this)
        .parents(".note-block")
        .attr("id")
        .match(/(?<=note_)\d*/)[0];
      var data = new FormData();
      var $note_block = $(this).parents(".note-block");
      data.append("note_id", note_id);
      e.stopPropagation();
      $.ajax({
        type: "POST",
        url: "/delete_note",
        data: data,
        cache: false,
        contentType: false,
        processData: false,
        success: function (response) {
          switch (response.code) {
            case 1:
              $note_block.remove();
              break;
            case 2:
              alert("Stop deleting other's notes");
              break;
            case 3:
              alert("Unknown error");
              break;
          }
        },
      });
    });
  $("#my_notes_only").on("click", function () {
    if ($(this).is(":checked")) {
      queryString.append("my_notes_only", "true");
    } else {
      queryString.delete("my_notes_only");
    }
    window.location.replace(
      window.location.pathname + "?" + queryString.toString()
    );
  });

  if (queryString.has("my_notes_only")) {
    $("#my_notes_only").prop("checked", true);
  }
})(jQuery);
