/*
  This file is to enable users on the coursetalk reviews
  page to both view and write reviews.
 */

export class CoursetalkReviews {  // eslint-disable-line import/prefer-default-export
  constructor() {
    const $coursetalkToggleReadWriteReviews = $(".toggle-read-write-reviews");
    const $coursetalkScriptObject = $(".coursetalk-reviews-script");

    const readSrc = "//d3q6qq2zt8nhwv.cloudfront.net/s/js/widgets/coursetalk-read-reviews.js";
    const writeSrc = "//d3q6qq2zt8nhwv.cloudfront.net/s/js/widgets/coursetalk-write-reviews.js";

    $coursetalkToggleReadWriteReviews.on('click', () => {
      // Cache js file for future button clicks
      $.ajaxSetup({cache: true});

      // Toggle the new coursetalk script object
      let currentSrc = $coursetalkScriptObject.attr("src");
      let newSrc = (currentSrc == readSrc) ? writeSrc : readSrc;
      $coursetalkScriptObject.attr("src", newSrc);
      $.getScript(newSrc);

      // Switch the button text
      let newText = (newSrc == readSrc) ? "View Reviews" : "Write a Review";
      $coursetalkToggleReadWriteReviews.text(newText);
    });
  }
}
