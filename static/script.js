document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('searchForm').addEventListener('submit', (e) => {
        e.preventDefault();
        alert('Search functionality is not implemented yet.');
    });

    document.getElementById('addToBag').addEventListener('click', () => {
        alert('Add to Bag functionality is not implemented yet.');
    });

    const loginForm = document.getElementById('loginForm');
    if (loginForm) {
        loginForm.addEventListener('submit', (e) => {
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;

            if (!email || !password) {
                e.preventDefault();
                alert('Please fill out all fields.');
            } else if (!email.includes('@')) {
                e.preventDefault();
                alert('Please enter a valid email.');
            }
        });
    }

    const registerForm = document.getElementById('registerForm');
    if (registerForm) {
        registerForm.addEventListener('submit', (e) => {
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;

            if (!name || !email || !password) {
                e.preventDefault();
                alert('Please fill out all fields.');
            } else if (!email.includes('@')) {
                e.preventDefault();
                alert('Please enter a valid email.');
            }
        });
    }
});
