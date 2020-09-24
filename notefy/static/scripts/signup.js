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


  function validateCheckbox () {
    var subject_checked = 0;
    $(".subject-category")
      .children("input")
      .each(function () {
        if ($(this).is(":checked")) {
          subject_checked++;
        }
      });
    if (subject_checked == 6) {
      $("#submit-button")
        .addClass("confirm-available")
        .attr("disabled", false);
    } else {
      $("#submit-button")
        .removeClass("confirm-available")
        .attr("disabled", true);
    }
  }

  validateCheckbox();

  $(".subject-category")
    .children("input")
    .on("click", function () {
      validateCheckbox();
    });
})(jQuery);
