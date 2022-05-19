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

//
// $(document).ready(function () {
//     restaurant();
// });
//
// function restaurant() {
//     $.ajax({
//         type: "GET",
//         url: "/resultdata",
//         data: {},
//         success: function (response) {
//             alert('success!')
//             let data = response['data']
//
//             for (let i=0; i<data.length; i++) {
//                 let number = i+1
//                 let name = data[i][0]
//                 let address = data[i][1]
//                 // let sort = data[i]['sort']
//                 // let menu = data[i]['menu']
//                 // let mean_price = data[i]['mean_price']
//                 let score = data[i][5]
//                 // let people_give_score = data[i]['people_give_score']
//                 // let review_count = data[i]['review_count']
//                 let review_list = (data[i][8]||'').split('/')
//                 let img_food = data[i][9]
//                 if (img_food == null) {
//                     img_food = '../static/assets/img/img_nothing.jpeg'
//                 } else {
//                     img_food = (data[i][9]||'').split(',')[0]
//                 }
//
//                 // let img_inner = data[i]['img_inner']
//
//                 let temp_html = `<h2 class="post-title" style="left">${number}. ${name}</h2>
//                                     <a href="https://map.naver.com/v5/search/${name}/place/" target="_blank">
//                                     <img src= "${img_food}"
//                                         class="food-img" style="float:left;">
//                                     <h3 class="post-score" style="float:right">평점: ${score}</h3>
//                                     <h3 class="post-address"">${address}</h3>
//
//                                     <p class="post-review">
//                                         ${review_list[0]}
//                                     </p>
//                                 </a>
//                                 <!-- Divider-->
//                                 <hr class="my-5" />`
//                 $('#restaurant-box').append(temp_html)
//             }
//         }
//     })
// }
