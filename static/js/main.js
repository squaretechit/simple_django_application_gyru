$(document).ready(function () {

  // back to top button start
  $(window).scroll(function () {
      if ($(this).scrollTop() > 40) {
          $('#backToTopBtn').fadeIn();
      } else {
          $('#backToTopBtn').fadeOut();
      }
  });

  $("#backToTopBtn").click(function () {
      $('html ,body').animate({
          scrollTop: 0
      }, 800);
  });
  // back to top button End

});