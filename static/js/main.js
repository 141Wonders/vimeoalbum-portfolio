var video01Player;
var $videoSrc; 

/*jQuery */
$(document).ready(function() {
  console.log("ready!");

  // Name Logo animation
  $('.logo-text').textyle({
    callback : function(){
      $(this).css({
        color : 'white',
        transition : '3s',
      });
    }
  });
  // About Page animations
  $('.bio-summary').hide();
  $('.bio-pic').css("cursor", "pointer").click(function(){
    $('.bio-summary').stop().slideToggle(2000).click(function(){
      $(this).stop().slideToggle(1000);
    });
  });

  // Gallery mouse events:
  $(".figure").css("cursor", "pointer");
  $(".figure-img").next().fadeTo(1,0.1);
  
  // hover over
  $(".figure-img").on('mouseenter', function(){
    $(this).next().stop().animate({
      fontSize: "1.2em",
      opacity: "1.0"
    },"slow");
    $(this).css("box-shadow", "0px 0px 8px #000");
  });
  // hover off
  $(".figure-img").on('mouseleave', function(){
    $(this).next().stop().animate({
      fontSize: "1.1em",
      opacity: "0.1"
    },"fast");
    $(this).css("box-shadow", "0px 0px 0px #ddd");
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