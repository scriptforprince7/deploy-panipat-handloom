(function ($) {
  "use strict";

   
  // Offcanvas menu
  $(".menu-trigger").on("click", function () {
    $(".extra-info,.offcanvas-overly").addClass("active");
    return false;
  });
  $(".menu-close,.offcanvas-overly").on("click", function () {
    $(".extra-info,.offcanvas-overly").removeClass("active");
  });

  // data-backround

  $("[data-background").each(function () {
    $(this).css(
      "background-image",
      "url( " + $(this).attr("data-background") + "  )"
    );
  });

  // Metis Menu 

  $("#mobile-menu").metisMenu();

  $('#hamburger').on('click', function() {            
    $('.mobile-nav').addClass('show');
    $('.overlay').addClass('active');
});

$('.close-nav').on('click', function() {            
    $('.mobile-nav').removeClass('show');            
    $('.overlay').removeClass('active');          
});

$(".overlay").on("click", function () {
    $(".mobile-nav").removeClass("show");
    $('.overlay').removeClass('active');
});


	// Sticky Header Js

  var windowOn = $(window);

	windowOn.on('scroll', function () {
		var scroll = windowOn.scrollTop();
		if (scroll < 400) {
			$("#header-sticky").removeClass("header-sticky");
		} else {
			$("#header-sticky").addClass("header-sticky");
		}
	});

  //jQuery Animation
  new WOW().init();

  // Nice select
  $("select").niceSelect();

  //Counter Up

  $(".counter-number span").counterUp({
    delay: 10,
    time: 1000,
  });

  //Magnific Pop-up

  $(".video-play-btn").magnificPopup({
    type: "iframe",
  });

  //Isotope Filter

  $(".port-menu li").on("click", function () {
    var selector = $(this).attr("data-filter");

    $(".port-menu li").removeClass("active");

    $(this).addClass("active");

    $(".portfolio-list").isotope({
      filter: selector,
      percentPosition: true,
    });
  });

  // Hero Area Slider

  $(".homepage-slides").owlCarousel({
    items: 1,
    dots: false,
    nav: true,
    loop: true,
    autoplay: false,
    autoplayTimeout: 5000,
    smartSpeed: 2000,
    slideSpeed: 600,
    navText: [
      "<i class='las la-arrow-left'></i>",
      "<i class='las la-arrow-right'></i>",
    ],
    responsive: {
      0: {
        items: 1,
        nav: false,
        dots: false,
      },
      600: {
        items: 1,
        nav: false,
        dots: false,
      },
      768: {
        items: 1,
      },
      1100: {
        items: 1,
      },
    },
  });

  $(".homepage-slides").on("translate.owl.carousel", function () {
    $(".single-slide-item h3")
      .removeClass("animated fadeInUp")
      .css("opacity", "1");
    $(".single-slide-item h1")
      .removeClass("animated fadeInDown")
      .css("opacity", "1");
    $(".single-slide-item p")
      .removeClass("animated fadeInUp")
      .css("opacity", "1");
    $(".single-slide-item .main-btn")
      .removeClass("animated fadeInDown")
      .css("opacity", "1");
  });

  $(".homepage-slides").on("translated.owl.carousel", function () {
    $(".single-slide-item h3")
      .addClass("animated fadeInUp")
      .css("opacity", "1");
    $(".single-slide-item h1")
      .addClass("animated fadeInDown")
      .css("opacity", "1");
    $(".single-slide-item p").addClass("animated fadeInUp").css("opacity", "1");
    $(".single-slide-item .main-btn")
      .addClass("animated fadeInDown")
      .css("opacity", "1");
  });

  // Project Slider

  $(".project-slider").owlCarousel({
    items: 1,
    dots: false,
    nav: false,
    loop: true,
    autoplay: true,
    autoplayTimeout: 5000,
    smartSpeed: 3000,
    slideSpeed: 300,
    margin: 30,
    navText: [
      "<i class='las la-arrow-left'></i>",
      "<i class='las la-arrow-right'></i>",
    ],
  });

  // Testimonial Slider

  $(".testimonial-wrapper").owlCarousel({
    items: 1,
    dots: false,
    nav: false,
    loop: true,
    autoplay: false,
    autoplayTimeout: 5000,
    smartSpeed: 3000,
    slideSpeed: 300,
    margin: 30,
    navText: [
      "<i class='las la-arrow-left'></i>",
      "<i class='las la-arrow-right'></i>",
    ],
  });

  // Feature Slider

  $(".feature_item").slick({
    speed: 8000,
    autoplay: true,
    autoplaySpeed: 1000,
    centerMode: true,
    cssEase: "linear",
    slidesToShow: 1,
    slidesToScroll: 1,
    variableWidth: true,
    infinite: true,
    initialSlide: 1,
    arrows: false,
    buttons: false,
  });

  // Project Slider Two

  $(".project-slider-two").owlCarousel({
    items: 1,
    dots: false,
    nav: true,
    loop: true,
    autoplay: false,
    autoplayTimeout: 5000,
    smartSpeed: 2000,
    slideSpeed: 600,
    navText: [
      "<i class='las la-arrow-left'></i>",
      "<i class='las la-arrow-right'></i>",
    ],
    responsive: {
      0: {
        items: 1,
        nav: false,
        dots: false,
      },
      600: {
        items: 1,
        nav: false,
        dots: false,
      },
      768: {
        items: 1,
      },
      1100: {
        items: 1,
      },
    },
  });

  // Client Slider

  $(".client-wrap").owlCarousel({
    loop: true,
    items: 5,
    dots: true,
    nav: false,
    smartSpeed: 500,
    autoHeight: false,
    touchDrag: true,
    mouseDrag: true,
    margin: 30,
    autoplay: false,
    responsive: {
      0: {
        items: 1,
        nav: false,
        dots: false,
      },
      600: {
        items: 2,
        nav: false,
        dots: false,
      },
      768: {
        items: 3,
        nav: false,
        dots: false,
      },
      1100: {
        items: 4,
        nav: false,
        dots: true,
      },
    },
  });

  // Testimonial Carousel Two

  $(".testimonial-carousel").owlCarousel({
    items: 1,
    margin: 30,
    dots: true,
    nav: false,
    loop: true,
    autoplay: true,
    responsiveClass: true,
    responsive: {
      575: {
        items: 1,
        nav: false,
        dots: false,
      },

      767: {
        items: 2,
        nav: false,
        dots: false,
      },

      990: {
        items: 2,
        loop: true,
      },
      1200: {
        items: 3,
        dots: true,
        loop: true,
      },
    },
  });

    // Portfolio Slider

    $(".portfolio-slider").owlCarousel({
      items: 1,
      margin: 30,
      dots: true,
      nav: false,
      loop: true,
      autoplay: true,
      responsiveClass: true,
      responsive: {
        575: {
          items: 1,
          nav: false,
          dots: false,
        },
  
        767: {
          items: 2,
          nav: false,
          dots: false,
        },
  
        990: {
          items: 2,
          loop: true,
        },
        1200: {
          items: 2,
          dots: true,
          loop: true,
        },
      },
    });
  

  //Progress Bar JS

  $("#bar1").barfiller({
    barColor: "#171717",
    duration: 5000,
  });

  $("#bar2").barfiller({
    barColor: "#171717",
    duration: 5000,
  });

  $("#bar3").barfiller({
    barColor: "#171717",
    duration: 5000,
  });

  $("#bar4").barfiller({
    barColor: "#171717",
    duration: 5000,
  });

  // Active & Remove Class

  $(".sub-menu ul li").on("click", function () {
    $(".sub-menu").removeAttribute("style");
    $(this).addClass("active");
  });

  $("a.nav-link").on("mouseover", function () {
    $("a.nav-link").removeClass("active");
    $(this).addClass("active");
  });

  //Hide Loading Box (Preloader)
  function handlePreloader() {
    if ($(".preloader").length) {
      $(".preloader").delay(200).fadeOut(500);
    }
  }

  $(window).on("load", function () {
    $(".portfolio-list").isotope({
      layoutMode: "masonry",
    });
  });

  $(window).on("load", function () {
    handlePreloader();
  });

  // Mouse Custom Cursor
  function itCursor() {
    var myCursor = jQuery(".mouseCursor");
    if (myCursor.length) {
      if ($("body")) {
        const e = document.querySelector(".cursor-inner"),
          t = document.querySelector(".cursor-outer");
        let n,
          i = 0,
          o = !1;
        (window.onmousemove = function (s) {
          o ||
            (t.style.transform =
              "translate(" + s.clientX + "px, " + s.clientY + "px)"),
            (e.style.transform =
              "translate(" + s.clientX + "px, " + s.clientY + "px)"),
            (n = s.clientY),
            (i = s.clientX);
        }),
          $("body").on("mouseenter", "button, a, .cursor-pointer", function () {
            e.classList.add("cursor-hover"), t.classList.add("cursor-hover");
          }),
          $("body").on("mouseleave", "button, a, .cursor-pointer", function () {
            ($(this).is("a", "button") &&
              $(this).closest(".cursor-pointer").length) ||
              (e.classList.remove("cursor-hover"),
              t.classList.remove("cursor-hover"));
          }),
          (e.style.visibility = "visible"),
          (t.style.visibility = "visible");
      }
    }
  }
  itCursor();
})(window.jQuery);
