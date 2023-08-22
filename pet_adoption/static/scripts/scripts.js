/*  Donate Page Scripts*/
document.addEventListener('DOMContentLoaded', () => {
  const donateButtons = document.querySelectorAll('.donate-amount');
  const customAmountInput = document.querySelector('.custom-amount');
  const donateButton = document.querySelector('.donate-button');
  const successMessage = document.getElementById('success-message');
  const userDataElement = document.getElementById('user-data');
  const user = userDataElement.getAttribute('data-logged-user');

  donateButtons.forEach(button => {
    button.addEventListener('click', () => {
      donateButtons.forEach(btn => btn.classList.remove('selected'));
      button.classList.add('selected');
      customAmountInput.value = ''; // Clear custom amount input
    });
  });

  donateButton.addEventListener('click', () => {
    let message = '';

    if (customAmountInput.value !== '' && customAmountInput.value > 0) {
      message += `Donation of $${customAmountInput.value}`;
    }

    const donateAmounts = document.querySelectorAll('.donate-amount[data-amount]');
    donateAmounts.forEach(amountDiv => {
      if (amountDiv.classList.contains('selected')) {
        message += ` Selected amount: $${amountDiv.getAttribute('data-amount')}`;
      }
    });

    // Add similar checks for other divs
    const otherDivs = document.querySelectorAll('.other-div-class');
    otherDivs.forEach(div => {
      if (div.textContent !== '' && div.textContent !== 0) {
        message += ` ${div.textContent}`;
      }
    });

    if (message !== '') {
      successMessage.textContent = `${message} successfully made. Thank you ${user}!`;
    } else {
      successMessage.textContent = 'Please select or enter a valid value.';
    }
  });
});