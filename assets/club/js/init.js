
        (function($) {
            "use strict";

            var unique_class = "stm-next-match-5495";

            var owl = $('.' + unique_class + ' .stm-next-match-units');

            $(document).ready(function() {
                owl.owlCarousel({
                    items: 1,
                    autoplay: false,
                    slideBy: 1
                });

                $('.' + unique_class + ' .stm-next-match-prev').on('click', function() {
                    owl.trigger('prev.owl.carousel');
                });

                $('.' + unique_class + ' .stm-next-match-next').on('click', function() {
                    owl.trigger('next.owl.carousel');
                });

                owl.on('changed.owl.carousel', function(event) {

                    var current = parseInt(event.item.index + 1);
                    var total = parseInt(event.item.count);

                    if (current == 1) {
                        $('.' + unique_class + ' .stm-next-match-prev').addClass('disabled');
                    } else {
                        $('.' + unique_class + ' .stm-next-match-prev').removeClass('disabled');
                    }

                    if (current === total) {
                        $('.' + unique_class + ' .stm-next-match-next').addClass('disabled');
                    } else {
                        $('.' + unique_class + ' .stm-next-match-next').removeClass('disabled');
                    }

                    $('.stm-next-match-pagination .current').text(current);
                })

            });
        })(jQuery);

        (function($) {
            "use strict";

            var owl = $('.stm-statistic-tabs .tab-pane.active .stm-player-statistic-unit');

            $(document).ready(function() {
                owl.owlCarousel({
                    items: 1,
                    dots: false,
                    autoplay: false,
                    slideBy: 1,
                    loop: false,
                    navText: ''
                });
            });

            $('.stm-statistic-tabs .stm-media-tabs-nav ul li a').on('shown.bs.tab', function() {
                var tabId = $(this).attr('href');
                var owlTab = $(tabId + ' .stm-player-statistic-unit');

                owlTab.owlCarousel({
                    items: 1,
                    dots: false,
                    autoplay: false,
                    slideBy: 1,
                    loop: false,
                    navText: ''
                });

                owlTab.trigger('destroy.owl.carousel');
                owlTab.html(owlTab.find('.owl-stage-outer').html()).removeClass('owl-loaded');

                owlTab.owlCarousel({
                    items: 1,
                    dots: false,
                    autoplay: false,
                    slideBy: 1,
                    loop: false,
                    navText: ''
                });
            });

        })(jQuery);

        (function($) {
            "use strict";

            var unique_class = "stm-players-9996";

            var owl = $('.' + unique_class + ' .stm-players');

            $(document).ready(function() {
                owl.owlCarousel({
                    items: 4,
                    dots: false,
                    autoplay: false,
                    slideBy: 4,
                    loop: true,
                    responsive: {
                        0: {
                            items: 1,
                            slideBy: 1
                        },
                        440: {
                            items: 2,
                            slideBy: 2
                        },
                        768: {
                            items: 3,
                            slideBy: 3
                        },
                        992: {
                            items: 3,
                            slideBy: 3
                        },
                        1100: {
                            items: 4,
                            slideBy: 4
                        }
                    }
                });

                $('.' + unique_class + ' .stm-carousel-control-prev').on('click', function() {
                    owl.trigger('prev.owl.carousel');
                });

                $('.' + unique_class + ' .stm-carousel-control-next').on('click', function() {
                    owl.trigger('next.owl.carousel');
                });
            });
        })(jQuery);

        (function($) {
            "use strict";

            var unique_class = "stm-product-carousel-init-4425";

            var unique_class_controls = "stm-product-carousel-controls-4097";

            var owl = $('.' + unique_class);

            $(window).load(function() {
                owl.owlCarousel({
                    items: 2,
                    dots: true,
                    autoplay: false,
                    loop: true,
                    slideBy: 2,
                    responsive: {
                        0: {
                            items: 1,
                            slideBy: 1
                        },
                        450: {
                            items: 2,
                            slideBy: 2
                        },
                        768: {
                            items: 2,
                            slideBy: 2
                        }
                    }
                });

                $('.' + unique_class_controls + ' .stm-carousel-control-prev').on('click', function() {
                    owl.trigger('prev.owl.carousel');
                });

                $('.' + unique_class_controls + ' .stm-carousel-control-next').on('click', function() {
                    owl.trigger('next.owl.carousel');
                });
            });
        })(jQuery);

        (function($) {
            "use strict";

            var unique_class = "stm-reviews-9848";

            var owl = $('.' + unique_class + ' .stm-reviews');

            $(document).ready(function() {
                owl.owlCarousel({
                    items: 1,
                    dots: true,
                    autoplay: true,
                    autoplayHoverPause: true,
                    loop: true,
                    slideBy: 1,
                    dotsContainer: '.' + unique_class + ' .stm-review-dots',
                    onTranslated: function() {
                        var image = $('.' + unique_class + ' .owl-item.active .stm-review-single').data('image');
                        $('.' + unique_class + ' .stm-review-image').css('background-image', 'url("' + image + '")');
                    }
                });

                $('.' + unique_class + ' .stm-carousel-control-prev').on('click', function() {
                    owl.trigger('prev.owl.carousel');
                });

                $('.' + unique_class + ' .stm-carousel-control-next').on('click', function() {
                    owl.trigger('next.owl.carousel');
                });
            });
        })(jQuery);
    
        /* <![CDATA[ */
        var sb_instagram_js_options = {
            "sb_instagram_at": "1498526473.3a81a9f.39fd996813ed4e78b08884d556e9df3e"
        };
        /* ]]> */
