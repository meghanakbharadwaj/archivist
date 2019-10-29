$(document).ready(function(){
    $('.customer-logos').slick({
      slidesToShow: 6,
      slidesToScroll: 1,
      autoplay: true,
      autoplaySpeed: 1000,
      arrows: true,
      dots: false,
      prevArrow:$(".prev"),//"<button type='button' class='slick-prev pull-left'><i class='fa fa-angle-left fa-4x' aria-hidden='true'></i></button>",
      nextArrow:$(".next"),//"<button type='button' class='slick-next pull-right'><i class='fa fa-angle-right fa-4x' aria-hidden='true'></i></button>",
      pauseOnHover: false,
      responsive: [{
        breakpoint: 768,
        settings: {
          slidesToShow: 4
        }
      }, {
        breakpoint: 520,
        settings: {
          slidesToShow: 3
        }
      }]
    });
  });