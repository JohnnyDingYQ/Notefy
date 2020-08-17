//animate the down arrow in main page. Credit to Codepen @Mika Furuse
var timer = 0
function animate_arrow(terminate){
	if (terminate) {
		clearTimeout(timer)
	}else{
		$(".scrolldown-arrow").animate({
			marginBottom: '-=15px'
		}, 800).animate({
			marginBottom: '+=15px'
		}, 800)
		timer = setTimeout('animate_arrow()', 1600)
	}
	
	
}
(function($) {

	//force scroll to top
	$(window).on("beforeunload", function(){
		$(window).scrollTop(0)
	})
	
	//initiate the animation loop
	setTimeout("animate_arrow(false)")

	//home page scroll down animation
	var has_scrolled_1 = false;
	$(window).scroll(function(){
		if (!has_scrolled_1) {
			if ($(window).scrollTop() > 200) {
				has_scrolled_1 = true
				//stop arrow animation
				$(".scrolldown-arrow").finish()
				setTimeout("animate_arrow(true)")
				//animate auto scroll 1
				$(".flex-container").animate({
					marginBottom: '+=1000px',
					opacity: '0'
				}, 400)
				$(".scrolldown-arrow").animate({
					marginBottom: '+=300px',
					opacity: '0'
				}, 800, function(){
					$(window).scrollTop(window.innerHeight + 1500)
					$(".showcase-container").animate({
						opacity: "1"
					}, 500)
				})
				
			}
		}
	})
	//login and signup button onclick
	$(".button-blue, .button-orange").on("click", function(){
		if ($(this).hasClass("button-blue")) {
			$(".escaper-1, .showcase-container, .scrolldown-arrow").toggle() //hide elements below to prevent scroll. Also hides arrow
			$(".login-shade").fadeIn(600).css("display", "flex")  //show shade and login/signup box
		}else{
			window.location.href = "/signup"
		}
	})


	//customize school select for student signup
	var schools  = ["YKPao School", "SUIS", "YKPao Secondary School", "Deep Dark Fantasy", "NOT YKPAO E", "New Spenceland", "Spenceloavania", "I need more e"]
	//add click event to newly added suggestions
	function bind_school_autocomplete(){
		$(".school-select").find("li").on("click", function(){
			$(".school-select").children("input").val($(this).text())
			$(".school-select").children("ul").empty().css("display", "none")
		})
	}

	var suggestion_list = $(".school-select").children("ul")
	$(".school-select").children("input").on("input", function(){
		suggestion_list.empty() //delete all suggestions before appending new ones
		if ($(this).val() !== "") {
			var found = false
			var user_input = $(this).val().toUpperCase()
			schools.forEach(function(item, index){
				if (item.toUpperCase().indexOf(user_input) !== -1) {
					suggestion_list.append("<li>" + item +"</li>")
					suggestion_list.css("display", "block") //show suggestions
					found = true
				}
				if (!found) {
					suggestion_list.css("display", "none")
				}
				bind_school_autocomplete()
			})
		}else{
			suggestion_list.css("display", "none") //hide suggestions
		}
	})
})(jQuery);