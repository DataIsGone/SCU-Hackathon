var jeremyFile = "/IndeedScraper.py"

function createCards() {
    var toAdd = document.createDocumentFragment();

    // TEST
    var cardContent =
    '<div class="mdl-card__media"></div>' + 
    '<div class="mdl-card__title">' +
        '<h2 class="mdl-card__title-text">Software Engineer (Backend - All Levels) - Santa Clara</h2>' +
    '</div>' +
    '<div>' +
        'You will be part of a small, close-knit team of 4-8 members including product and engineering that owns a piece of the product and evolves it with its own goals…' +
    '</div>' +
    '<div class="mdl-card__actions">' +
        '<a class="mdl-button mdl-button--colored mdl-js-button mdl-js-ripple-effect mdl-button--accent" href="http://www.indeed.com/rc/clk?jk=20d830a94ab8c6ef&amp;from=vj&amp;pos=bottom" data-upgraded=",MaterialButton,MaterialRipple">Read more<span class="mdl-button__ripple-container"><span class="mdl-ripple"></span></span></a>' +
    '</div>'

    for(var i=0; i < 11; i++){ // Replace 11 with number from Jeremy's aggregator
        var newDiv = document.createElement('div');
        newDiv.id = 'job' + i;
        newDiv.className = 'jobcard';
        newDiv.innerHTML = newDiv.id;
        toAdd.appendChild(newDiv);
        newDiv.innerHTML = cardContent
    }
    document.body.appendChild(toAdd);
}
