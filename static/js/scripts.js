document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    const numbersInput = document.getElementById('numbers');
    const submitButton = document.querySelector('button[type="submit"]');
    const spinner = document.createElement('div');
    spinner.className = 'spinner-border text-primary';
    spinner.style.display = 'none';
    submitButton.parentNode.insertBefore(spinner, submitButton.nextSibling);

    form.addEventListener('submit', function(event) {
        spinner.style.display = 'inline-block';
        submitButton.disabled = true;
    });

    numbersInput.addEventListener('input', function() {
        if (numbersInput.value.trim() === '') {
            submitButton.disabled = true;
        } else {
            submitButton.disabled = false;
        }
    });
});
