
var $details_tab_item=$(".details-tab");
var $details_info_item=$(".details-info")

$details_tab_item.each(function(){
	$(this).click(
		function(){
			// $(this).removeClass("tab-onclick")
			var index=$(this).index();
			// $(".details-tab").eq(index).addClass("tab-onclick");
			$details_tab_item.each(function(){
				$(this).removeClass("tab-onclick");
			});
			$(this).addClass("tab-onclick");
			$details_info_item.each(function(){
				$(".details-info-tab").removeClass("info-show");
				$(".details-info-tab").eq(index).addClass("info-show");
			});
		}
		);
});
