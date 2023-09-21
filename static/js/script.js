const cardCarousels = document.querySelectorAll('.card-stack-carousel');

cardCarousels.forEach(function (cardCarousel) {
  
  // Carousel Variables
  let cardCollection = cardCarousel.querySelectorAll('.card-stack-carousel__card');
  let cardCollectionSize = cardCollection.length - 1;
  let carouselIndicators = cardCarousel.querySelectorAll('.card-stack-carousel__indicators li');
  let cardObject
  
  // Add Event Listener for Carousel Indicators
  carouselIndicators.forEach(function (indicator, index) {
    indicator.addEventListener('click', function (e) {
      cardObject = cardCarousel.getElementsByClassName('card-stack-carousel__card').item(index);
      clearCardStackCarousel(cardCollection);
      initCardStackCarousel(cardObject, cardCollection, cardCollectionSize, index);
    });
  });
  
  // Add Event Listener for Card Click
  cardCollection.forEach(function (card, index) {
    cardObject = card;
    // Initialize carousel
    if(card.classList.contains('active') && !card.parentNode.classList.contains('initialized')) {
      initCardStackCarousel(cardObject, cardCollection, cardCollectionSize, index);
      card.parentNode.classList.add('initialized');
    }
    card.addEventListener('click', function (event) {
      clearCardStackCarousel(cardCollection);
      initCardStackCarousel(cardObject, cardCollection, cardCollectionSize, index);
    });
  });
  
  // Automatically loop through cards
  if(cardCarousel.getAttribute("data-interval") == 'true') {
    window.setInterval(nextCard, 6000);
  }
  
  // Clear classes
  function clearCardStackCarousel() {
    cardCollection.forEach(function (card) {
      card.classList.remove('active', 'prev', 'next', 'first', 'last');
    });
  }
  
  // Initialize carousel
  function initCardStackCarousel(cardObject, cardCollection, cardCollectionSize, index) {
    
      cardCarousel.getElementsByClassName('card-stack-carousel__card').item(index).classList.add('active');
    
      // Previous
      if(index == 0) {
        cardCollection[cardCollectionSize].classList.add('prev');
        if(cardCollectionSize > 4) {
          cardCollection[cardCollectionSize - 1].classList.add('first');
        }
      } else {
        cardCollection[index - 1].classList.add('prev');
        if(cardCollectionSize > 4) {
          if(index - 1 == 0) {
            cardCollection[cardCollectionSize].classList.add('first');
          } else {
            cardCollection[index - 2].classList.add('first');
          }
        }
      }
    
      // Next
      if(index == cardCollectionSize) {
        cardCollection[0].classList.add('next');
        if(cardCollectionSize > 4) {
          cardCollection[1].classList.add('last');
        }
      } else {
        cardCollection[index + 1].classList.add('next');
        if(cardCollectionSize > 4) {
          if(index + 1 == cardCollectionSize) {
            cardCollection[0].classList.add('last');
          } else {
            cardCollection[index + 2].classList.add('last');
          }
        }
      }
  }
  
  // Next click
  function nextCard() {
    cardCarousel.querySelector('.card-stack-carousel__card.next').click();
  }
  // Prev click
  function prevCard() {
    cardCarousel.querySelector('.card-stack-carousel__card.prev').click();
  }
  
});