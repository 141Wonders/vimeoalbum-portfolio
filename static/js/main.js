var video01Player;
var $videoSrc; 

/*jQuery */
$(document).ready(function() {
  console.log("ready!");

  $('.logo-text').textyle({
    callback : function(){
      $(this).css({
        color : 'white',
        transition : '3s',
      });
    }
  });

  $(".figure").css("cursor", "pointer");
  /* hover function for thumbnail elements */
  // $(".figure").hover(function(){
  //   $(this).stop().animate({
  //     "width" : "=+50"
  //   })
  // }, function(){
  //   $(this).stop().animate({
  //         "width" : "=-50"
  //       })
  // });

  $(".figure-img").on('mouseenter', function(){
    $(this).next().stop().animate({
      fontSize: "1.15em",
      opacity: "0.9"
    },"slow");

    // $(this).stop().fadeTo(500, 1);
  });

  $(".figure-img").on('mouseleave', function(){
    $(this).next().stop().fadeTo(500,0.2).animate({
      fontSize: "1.1em",
      opacity: "0.2"
    },"fast");
    // $(this).stop().fadeTo(500, 1);
  });

  /* Close buttton for nav overlay, will unload and destroy player */
  $(".closebtn").click(function(){
    video01Player.unload().then(function(){
      //video was unloaded
    }).catch(function(error) {
      //error occurred
    });
    video01Player.destroy();
    document.getElementById("myNav").style.width = "0%";
  });

  /* Load player function, retrieves url corresponding to its element*/
  $(".video-btn").click(function(){
      $videoSrc = $(this).data( "src" );
      console.log($videoSrc);

    var options01 = {
      url: $videoSrc,
      width:800
    };

    video01Player = new Vimeo.Player("Vimeo_Player", options01);

    video01Player.setVolume(1);

    video01Player.on('play', function() {
      console.log('Played the first video');
    });
    document.getElementById("myNav").style.width = "100%";
  });
});