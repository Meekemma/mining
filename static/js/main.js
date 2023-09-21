    



    const calculate = document.querySelector('#calculate');
    const starter = document.querySelector('#starter');
    const purchase = document.querySelector('#purchase');
    const money = document.querySelector('#money');
    const myForm = document.querySelector('#my-form');
    const amountInput = document.querySelector('#amount');
    const resultInput = document.querySelector('#result');
    const closeStarterBtn = document.querySelector('#close-starter');
    const closeMoneyBtn= document.querySelector('#close-money');



    const goldCalculate = document.querySelector('#gold-calculate');
    const goldStarter = document.querySelector('#gold-starter');
    const goldPurchase = document.querySelector('#gold-purchase');
    const goldMoney = document.querySelector('#gold-money');
    const goldMyForm = document.querySelector('#gold-my-form');
    const goldAmountInput = document.querySelector('#gold-amount');
    const goldResultInput = document.querySelector('#gold-result');
    const closeGoldStarterBtn = document.querySelector('#close-gold-starter');
    const closeGoldMoneyBtn = document.querySelector('#close-gold-money');




    const premiumCalculate = document.querySelector('#premium-calculate');
    const premium = document.querySelector('#premium');
    const premiumPurchase = document.querySelector('#premium-purchase');
    const premiumMoney = document.querySelector('#premium-money');
    const premiumForm = document.querySelector('#premium-form');
    const premiumAmountInput = document.querySelector('#premium-amount');
    const premiumResultInput = document.querySelector('#premium-result');
    const closePremiumBtn = document.querySelector('#close-premium');
    const closePremiumMoneyBtn = document.querySelector('#close-premium-money');


    calculate.addEventListener('click', function() {
        starter.style.display = 'block';
        money.style.display = 'none';
        goldMoney.style.display ='none'
        goldStarter.style.display = 'none'
        premium.style.display = 'none'
        premiumMoney.style.display ='none'
        goldStarter.style.display = 'none';

    });

    purchase.addEventListener('click', function() {
        money.style.display = 'block';
        starter.style.display = 'none';
        goldStarter.style.display = 'none';
        goldMoney.style.display = 'none';
        premium.style.display = 'none';
        premiumMoney.style.display = 'none';
        });

    goldCalculate.addEventListener('click', function() {
        goldStarter.style.display = 'block';
        goldMoney.style.display = 'none';
        starter.style.display = 'none';
        money.style.display = 'none';
        premium.style.display = 'none';
        premiumMoney.style.display = 'none';
    });
        
    goldPurchase.addEventListener('click', function() {
        goldMoney.style.display = 'block';
        goldStarter.style.display = 'none';
        starter.style.display = 'none';
        money.style.display = 'none';
        premium.style.display = 'none';
        premiumMoney.style.display = 'none';
    });
    
    premiumCalculate.addEventListener('click', function() {
        premium.style.display = 'block';
        premiumMoney.style.display = 'none';
        starter.style.display = 'none';
        money.style.display = 'none';
        goldStarter.style.display = 'none';
        goldMoney.style.display = 'none';
    });
    
    premiumPurchase.addEventListener('click', function() {
        premiumMoney.style.display = 'block';
        premium.style.display = 'none';
        starter.style.display = 'none';
        money.style.display = 'none';
        goldStarter.style.display = 'none';
        goldMoney.style.display = 'none';
    });    


    closeStarterBtn.addEventListener('click', function() {
        starter.style.display = 'none';
    });

    closeMoneyBtn.addEventListener('click', function() {
        money.style.display = 'none';
    });

    myForm.addEventListener('submit', onSubmit);

    function onSubmit(e) {
        e.preventDefault();

        if (amountInput.value >= 500 && amountInput.value <= 999) {
            const newAmount = amountInput.value * 6;
            resultInput.value = `$${newAmount} earned after 3 days`;
        }else if (amountInput.value <= 499) {
            alert('Please enter an amount of $500 or more.');
        } else {
            alert('Please enter an amount lesser than 1000.');
        }
    }




    
    
    goldCalculate.addEventListener('click', function() {
        goldStarter.style.display = 'block';
        goldMoney.style.display = 'none';
    });
    
    goldPurchase.addEventListener('click', function() {
        goldMoney.style.display = 'block';
        goldStarter.style.display = 'none';
    });
    
    closeGoldStarterBtn.addEventListener('click', function() {
        goldStarter.style.display = 'none';
    });
    
    closeGoldMoneyBtn.addEventListener('click', function() {
        goldMoney.style.display = 'none';
    });
    
    goldMyForm.addEventListener('submit', onGoldSubmit);
    
    function onGoldSubmit(e) {
        e.preventDefault();
    
        if (goldAmountInput.value >= 1000 && goldAmountInput.value <= 1999) {
            const newAmount = goldAmountInput.value * 7;
            goldResultInput.value = `$${newAmount} earned after 5 days`;
        } else if (goldAmountInput.value <= 999) {
            alert('Please enter an amount of $1000 or more.');
        } else {
            alert('Please enter an amount lesser than 2000.');
        }
    }




    
    
    
    premiumCalculate.addEventListener('click', function() {
        premium.style.display = 'block';
        premiumMoney.style.display = 'none';
    });
    
    premiumPurchase.addEventListener('click', function() {
        premiumMoney.style.display = 'block';
        premium.style.display = 'none';
    });
    
    closePremiumBtn.addEventListener('click', function() {
        premium.style.display = 'none';
    });
    
    closePremiumMoneyBtn.addEventListener('click', function() {
        premiumMoney.style.display = 'none';
    });
    
    premiumForm.addEventListener('submit', onPremiumSubmit);
    
    function onPremiumSubmit(e) {
        e.preventDefault();
    
        if (premiumAmountInput.value >= 2000 && premiumAmountInput.value <= 9999) {
            const newAmount = premiumAmountInput.value * 7.75;
            premiumResultInput.value = `$${newAmount} earned after 7 days`;
        } else if (premiumAmountInput.value <= 1999) {
            alert('Please enter an amount of $2000 or more.');
        } else {
            alert('Please enter an amount lesser than 10000.');
        }
    }
    


    