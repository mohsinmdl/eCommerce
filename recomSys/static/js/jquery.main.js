

// page init
jQuery(function(){
	"use strict";

	initIsoTop();
	initbackTop();
	initCounter();
	initAddClass();
	initCountDown();
	initSlickSlider();
	initStickyHeader();
});

jQuery(window).on('load', function() {
	"use strict";

	initIsoTop();
	initPreLoader();
	new WOW().init();
	initStyleChanger();
});



// count down init
function initCountDown() {
	var newDate = new Date(2018, 12, 28);
	
	jQuery("#defaultCountdown").countdown({until: newDate});
}

function initAddClass() {
	jQuery(".btn-search, .close-btn").click(function() {
		jQuery("body").toggleClass("search-active");
	});
	jQuery(".nav-opener").click(function() {
		jQuery(".nav-holder").toggleClass("nav-active");
	});
	jQuery(".cart-box").click(function() {
		jQuery(".icon-list").toggleClass("cart-active");
	});
	jQuery(".user-box").click(function() {
		jQuery(".icon-list").toggleClass("user-active");
	});
}

function initSlickSlider() {
	jQuery('#main-slider').slick({
		dots: true,
		arrows: false,
		autoplay: true,
		speed: 800,
		infinite: true,
		adaptiveHeight: true,
		fade: true,
		autoplaySpeed: 4000
	});
	jQuery('.blockquote-slider').slick({
		autoplay: true,
		adaptiveHeight: true
	});
	jQuery('.team-slider').slick({
		dots: true,
		autoplay: true,
		slidesToShow: 3,
		slidesToScroll: 1,
		adaptiveHeight: true,
		responsive: [
		{
		  breakpoint: 1024,
		  settings: {
		  	dots: true,
		    slidesToShow: 3,
		    slidesToScroll: 3,
		    infinite: true
		  }
		},
		{
		  breakpoint: 767,
		  settings: {
		    slidesToShow: 2,
		    slidesToScroll: 2
		  }
		},
		{
		  breakpoint: 480,
		  settings: {
		    dots: false,
		    slidesToShow: 1,
		    slidesToScroll: 1
		  }
		}
		]
	});
	jQuery('.slider-sec .slick-slider').slick({
		dots: true,
		arrows: true,
		slidesToShow: 1,
		centerMode: true,
		centerPadding: '30%',
		responsive: [
		{
			breakpoint: 768,
			settings: {
				arrows: false,
				centerMode: true,
				centerPadding: '20%',
				slidesToShow: 1
			}
		},
		{
			breakpoint: 480,
			settings: {
				arrows: false,
				centerMode: true,
				centerPadding: '20%',
				slidesToShow: 1
			}
		}
		]
	});
	jQuery('.product-slider').slick({
		slidesToShow: 1,
		slidesToScroll: 1,
		arrows: false,
		fade: true,
		centerPadding: '0',
		asNavFor: '.pagg-slider'
	});
	jQuery('.pagg-slider').slick({
		slidesToShow: 4,
		slidesToScroll: 1,
		centerPadding: '0',
		asNavFor: '.product-slider',
		focusOnSelect: true
	});
}

// IsoTop init
function initIsoTop() {
	// Isotope init
	var isotopeHolder = jQuery('#masonry-container'),
		win = jQuery(window);
	jQuery('#masonry-container').isotope({
		itemSelector: '.product-block',
		transitionDuration: '0.6s'
	});
	jQuery('.filter-list a').click(function(e){
		e.preventDefault();
		
		jQuery('.filter-list li').removeClass('active');
		jQuery(this).parent('li').addClass('active');
		var selector = jQuery(this).attr('data-filter');
		isotopeHolder.isotope({ filter: selector });
	});
}

// sticky header init
function initbackTop() {
	var jQuerybackToTop = jQuery("#back-top");
	jQuery(window).on('scroll', function() {
		if (jQuery(this).scrollTop() > 100) {
			jQuerybackToTop.addClass('active');
		} else {
			jQuerybackToTop.removeClass('active');
		}
	});
	jQuerybackToTop.on('click', function(e) {
		jQuery("html, body").animate({scrollTop: 0}, 500);
	});
}

// PreLoader init
function initPreLoader() {
	jQuery('#pre-loader').delay(400).fadeOut();
}

// style changer
function initStyleChanger() {
	var element = jQuery('#style-changer');

	if(element) {
		$.ajax({
			url: element.attr('data-src'),
			type: 'get',
			dataType: 'text',
			success: function(data) {
				var newContent = jQuery('<div>', {
					html: data
				});

				newContent.appendTo(element);
				jQuery(".changer-opener").click(function(event){
					event.preventDefault();
					jQuery("body").toggleClass("changer-active");
				});
				
				var sheet,
					darkSheet,
					sheetName,
					darkSheetName = 'dark',
					sheetAdded = false,
					darkStylesAdded = false;

				jQuery('.list-color li').each(function() {
					var item = jQuery(this),
						link = item.find('a').eq(0);

					link.on('click', function(e) {
						e.preventDefault();
						sheetName = item.attr('class');

						if(!sheetAdded) {
							sheet = jQuery('<link>').attr('rel','stylesheet')
										.attr('type','text/css')
										.attr('href', 'css/color/' + sheetName + '.css')
										.appendTo('head');

							sheetAdded = true;
						} else {
							sheet.attr('href', 'css/color/' + sheetName + '.css');
						}
					});
				});
			}
		});
	}
}


// sticky header init
function initStickyHeader() {
	var win = jQuery(window),
		stickyClass = 'sticky';

	jQuery('#header.sticky-header').each(function() {
		var header = jQuery(this);
		var headerOffset = header.offset().top || 0;
		var flag = true;

		function scrollHandler() {
			if (win.scrollTop() > headerOffset) {
				if (flag){
					flag = false;
					header.addClass(stickyClass);
				}
			} else {
				if (!flag) {
					flag = true;
					header.removeClass(stickyClass);
				}
			}

			ResponsiveHelper.addRange({
				'..767': {
					on: function() {
						header.removeClass(stickyClass);
					}
				}
			});
		}

		scrollHandler();
		win.on('scroll resize orientationchange', scrollHandler);
	});
}

// Counter init
function initCounter() {
	jQuery('.counter').counterUp({
		delay: 10,
		time: 2000
	});
}
