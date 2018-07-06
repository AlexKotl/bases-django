$(function() {
	$("#slides").slidesjs({
		width: 828,
		height: 130,
		navigation: false,
		pagination: false,
		play: {
			active: false,
			interval: 10000,
			auto: true,
			pauseOnHover: true,
			restartDelay: 10000
		}
	});

});