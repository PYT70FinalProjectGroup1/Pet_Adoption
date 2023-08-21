/*  Donate Page Scripts*/
document.addEventListener('DOMContentLoaded', () => {
  const donateButtons = document.querySelectorAll('.donate-amount');
  const donateButton = document.querySelector('.donate-button');
  const successMessage = document.getElementById('success-message');
  const userDataElement = document.getElementById('user-data');
  const user = userDataElement.getAttribute('data-logged-user');

  donateButtons.forEach(button => {
    button.addEventListener('click', () => {
      donateButtons.forEach(btn => btn.classList.remove('selected'));
      button.classList.add('selected');
    });
  });

  donateButton.addEventListener('click', () => {
    const selectedButton = document.querySelector('.donate-amount.selected');
    if (selectedButton) {
      const amount = selectedButton.getAttribute('data-amount');
      successMessage.textContent = `Donation of $${amount} successfully made. Thank you ${user}!`;
    }
  });
});