(function ($) {
  $(".subject-nav").on("click", function () {
    if (!$(this).hasClass("subject-nav-selected")) {
      $(".subject-nav").removeClass("subject-nav-selected");
      $(this).addClass("subject-nav-selected");
      let category = $(this).attr("name");
      $(".subject-category").css("display", "none");
      $("#" + category).css("display", "flex");
    }
  });

  function client_validation() {
    // TODO: Client side validation
  }

  $(".subject-category")
    .children("input")
    .on("click", function () {
      var subject_checked = 0;
      $(".subject-category")
        .children("input")
        .each(function () {
          if ($(this).is(":checked")) {
            subject_checked++;
          }
        });
      if (subject_checked == 6) {
        $("#submit-button").addClass("confirm-available");
      } else {
        $("#submit-button").removeClass("confirm-available");
      }
    });

  $("#submit-button").on("click", function () {
    if ($(this).hasClass("confirm-available")) {
      let subjects = [];
      $(".subject-category")
        .children("input")
        .each(function () {
          if ($(this).is(":checked")) {
            subjects.push($(this).attr("id"));
          }
        });
      var user_data = { user: {} };
      user_data.user.username = $("#username").val();
      user_data.user.email = $("#email").val();
      user_data.user.password = $("#password").val();
      user_data.user.subjects = subjects;
      $.ajax({
        type: "POST",
        url: "/signup",
        data: { data: JSON.stringify(user_data) },
        success: function (response) {},
      });
    }
  });
})(jQuery);
