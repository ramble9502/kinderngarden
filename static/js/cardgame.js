var CardGame = function() {

    var cards = [];
    var numberOfCards;
    var cardHTML;
    var nrOfClicks = 0;
    var preventClick = false;
    var selectedCards = [];
    var canPlay = false;
    var counter = 0;

    $('.playground').addClass('game-stop');


    function stopGame() {
        canPlay = false;
        $('.playground').addClass('game-stop');
    }

    function startGame() {
        canPlay = true;
        $('.playground').removeClass('game-stop');
    }

    function showAllCards(duration) {
        $('.c-card-flip.is-active').addClass("is-visible");
        setTimeout(function() {
            $('.c-card-flip.is-active').removeClass("is-visible");
            $('.js-show-all').removeClass('is-active');
        }, duration);
    }

    function updateProgress(myCards) {

        preventClick = true;

        if (myCards[0].attr('card-number') === myCards[1].attr('card-number')) {
            myCards[0].addClass('is-correct').removeClass("is-active");
            myCards[1].addClass('is-correct').removeClass("is-active");
        }
        nrOfClicks = 0;
        selectedCards = [];

        setTimeout(function() {
            $(".c-card-flip").removeClass("is-visible");
            preventClick = false;
        }, 600);

    }

    function generateCardArray(nrOfCard) {

        var i = 1;

        for (i; i <= nrOfCard / 2; i++) {
            var randomnum = Math.floor(Math.random() * 8000);
            cards.push(randomnum);
            cards.push(randomnum);
        }

    }

    function createCards(nrOfCard) {

        var i = 1;
        numberOfCards = nrOfCard;

        generateCardArray(numberOfCards);

        for (i; i <= numberOfCards; i++) {

            var cardNumber = cards[Math.floor(Math.random() * cards.length)];
            var cardIndex = cards.indexOf(cardNumber);
            cards.splice(cardIndex, 1);

            cardHTML = "<article class='c-card-flip is-active js-card-flip' card-number='" + cardNumber + "'>" +
                "<div class='c-card-flip__flipper'>" +
                "<div class='c-card-flip__front'>" +
                "</div>" +
                "<div class='c-card-flip__back'>" +
                "<h3 class='c-card-flip__title'>" +
                cardNumber +
                "</h3>" +
                "</div>" +
                "</div>" +
                "</article>";

            $('.playground__container').append(cardHTML);
        }

    }

    function activateCards() {

        $(document).on('click', '.c-card-flip.is-active', function() {
            if (!preventClick && canPlay) {

                $(this).toggleClass("is-visible");
                selectedCards.push($(this));

                if (nrOfClicks < 1) {
                    nrOfClicks++;
                } else {
                    updateProgress(selectedCards);
                }
            }
        });

    }

    function restartGame() {

        $('.playground__container').html('<span class="please-wait">GAME IS RESTARTING ...</span>');

        setTimeout(function() {
            $('.playground__container').html('');
            createCards(16);
            activateCards();
            $('.js-menu-item').removeClass('is-active');
        }, 3000);

    }

    return {
        createCards: createCards,
        activateCards: activateCards,
        showAllCards: showAllCards,
        startGame: startGame,
        stopGame: stopGame,
        restartGame: restartGame
    };

}();

CardGame.createCards(16);
CardGame.activateCards();

$('.js-menu-item').on('click', function() {
    $('.js-menu-item').removeClass('is-active');
    $(this).addClass('is-active');
});

$(document).on('click', '.js-show-all', function() {
    CardGame.showAllCards(2000);
});

$(document).on('click', '.js-start-game', function() {
    CardGame.startGame();
});

$(document).on('click', '.js-pause-game', function() {
    CardGame.stopGame();
});

$(document).on('click', '.js-restart-game', function() {
    CardGame.restartGame();
});
