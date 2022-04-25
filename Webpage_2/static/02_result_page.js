/*!
* Start Bootstrap - Clean Blog v6.0.8 (https://startbootstrap.com/theme/clean-blog)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-clean-blog/blob/master/LICENSE)
*/
window.addEventListener('DOMContentLoaded', () => {
    let scrollPos = 0;
    const mainNav = document.getElementById('mainNav');
    const headerHeight = mainNav.clientHeight;
    window.addEventListener('scroll', function() {
        const currentTop = document.body.getBoundingClientRect().top * -1;
        if ( currentTop < scrollPos) {
            // Scrolling Up
            if (currentTop > 0 && mainNav.classList.contains('is-fixed')) {
                mainNav.classList.add('is-visible');
            } else {
                mainNav.classList.remove('is-visible', 'is-fixed');
            }
        } else {
            // Scrolling Down
            mainNav.classList.remove(['is-visible']);
            if (currentTop > headerHeight && !mainNav.classList.contains('is-fixed')) {
                mainNav.classList.add('is-fixed');
            }
        }
        scrollPos = currentTop;
    });
})
// $(document).ready(function () {
//                 restaurant();
//             });
//
// function restaurant() {
//     $.ajax({
//         type: "GET",
//         url: "result",
//         data: {},
//         success: function (response) {
//             let data = response['data']
//
//             for (let i=0; i<data.length; i++) {
//                 let name = data[i]['name']
//
//                 let temp_html = `<a href="post.html">
//                                     <img src="https://search.pstatic.net/common/?autoRotate=true&quality=95&type=f180_180&src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTEwMjJfMTE5%2FMDAxNjM0ODQwMzE5NzE2.fIiBiGP57IGho5PAmqnX9_VJnTN6PtgHqoyHW8IiUKkg.jLcut4IzhBCtla-ktYSDIMwsbrd0UAKD89y3fXx-h_Mg.JPEG.kuk5837%2FIMG_0666.jpg,https://search.pstatic.net/common/?autoRotate=true&quality=95&type=f180_180&src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTA3MzFfMjEx%2FMDAxNjI3NzE0MzY0OTA0.p_oJLnns5VKJJln4CV8U5iq_vwVxVrDTaXSq6zpO900g.bzrqHMpeHP0SCragLb0sXqA1mseQt8-9TACJEegc70Yg.JPEG.9120afz%2FIMG_1112.jpg"
//                                         class="food-img" style="float:left;">
//                                     <h2 class="post-title">${name}</h2>
//                                     <h3 class="post-subtitle"">서울특별시 강남구 언주로164길 35 로로</h3>
//                                 </a>
//                                 <p class="post-meta">
//                                     리뷰리뷰리뷰리뷰
//                                 </p>
//                                 <!-- Divider-->
//                                 <hr class="my-4" />`
//
//
//                 $('#post-preview').append(temp_html)
//             }
//         }
//     })
// }
