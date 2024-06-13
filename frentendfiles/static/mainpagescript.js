// // script.js
// function showPage(page) {
//     const pageContainer = document.getElementById("pageContainer");

//     // Clear previous content
//     pageContainer.innerHTML = "";

//     if (page === 'login') {
//         pageContainer.innerHTML = `
//             <h1>Login</h1>
//             <form onsubmit="return handleLogin()">
//                 <!-- Your Login Form Fields Here -->
//                 <label for="loginUsername">Username:</label>
//                 <input type="text" id="loginUsername" name="loginUsername" required>

//                 <label for="loginPassword">Password:</label>
//                 <input type="password" id="loginPassword" name="loginPassword" required>

//                 <button type="submit">Login</button>
//             </form>
//         `;
//     } else if (page === 'signup') {
//         pageContainer.innerHTML = `
//             <h1>Sign Up</h1>
//             <form onsubmit="return handleSignUp()">
//                 <!-- Your Sign Up Form Fields Here -->
//                 <label for="signupFirstName">First Name:</label>
//                 <input type="text" id="signupFirstName" name="signupFirstName" required>

//                 <label for="signupLastName">Last Name:</label>
//                 <input type="text" id="signupLastName" name="signupLastName" required>

//                 <label for="signupEmail">Email:</label>
//                 <input type="email" id="signupEmail" name="signupEmail" required>
//                 <label for="signupPassword">Password:</label> <!-- Ensure correct ID for password field -->
//                  <input type="password" id="signupPassword" name="signupPassword" required> <!-- Ensure correct ID for password field -->

//                 <button type="submit" id ="index.html" >Sign Up</button>
//             </form>
//         `;
//     }
// }

// function handleLogin() {
//     const username = document.getElementById("loginUsername").value;
//     const password = document.getElementById("loginPassword").value;

//     // Check if the username and password match (dummy data for illustration)
//     if (username === "user" && password === "password") {
//         // Save login data to localStorage
//         localStorage.setItem("loggedInUser", username);

//         // Add logic for navigation (e.g., redirect to the next page)
//         alert("Login successful! Navigating to the next page.");
//     } else {
//         alert("Invalid username or password");
//     }

//     return false; // Prevent form submission for this example
// }

// function handleSignUp() {
//     // Dummy data for illustration
//     const firstName = document.getElementById("signupFirstName").value;
//     const lastName = document.getElementById("signupLastName").value;
//     const email = document.getElementById("signupEmail").value;
//     const password = document.getElementById("signupPassword").value;

//     // Save sign-up data to localStorage (dummy data for illustration)
//     localStorage.setItem("signedUpUser", JSON.stringify({ firstName, lastName, email }));

//     alert("Sign Up successful!")

//     return false; // Prevent form submission for this example
// }
// script.js
async function handleLogin() {
    const username = document.getElementById("loginUsername").value;
    const password = document.getElementById("loginPassword").value;

    // Send a POST request to the API with the login data
    const response = await fetch("https://your-api-url.com/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ username, password })
    });

    // Check if the response is successful
    if (response.ok) {
        // Save login data to localStorage
        const userData = await response.json();
        localStorage.setItem("loggedInUser", JSON.stringify(userData));

        // Redirect to a new page
        window.location.href = "newpage.html"; // Change "newpage.html" to the URL of the new page
    } else {
        alert("Invalid username or password");
    }

    return false; // Prevent form submission for this example
}

async function handleSignUp() {
    const firstName = document.getElementById("signupFirstName").value;
    const lastName = document.getElementById("signupLastName").value;
    const email = document.getElementById("signupEmail").value;
    const password = document.getElementById("signupPassword").value;

    // Send a POST request to the API with the sign-up data
    const response = await fetch("https://your-api-url.com/signup", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ firstName, lastName, email, password })
    });

    // Check if the response is successful
    if (response.ok) {
        alert("Sign Up successful!");
    } else {
        alert("Sign Up failed");
    }

    return false; // Prevent form submission for this example
}

function showPage(page) {
    const pageContainer = document.getElementById("pageContainer");

    // Clear previous content
    pageContainer.innerHTML = "";

    if (page === 'login') {
        pageContainer.innerHTML = `
          <h1>Login</h1>
            <form action="/">
                <!-- Your Login Form Fields Here -->
                <label for="loginUsername">Username:</label>
                <input type="text" id="loginUsername" name="loginUsername" required>

                <label for="loginPassword">Password:</label>
                <input type="password" id="loginPassword" name="loginPassword" required>

                <button type="submit">Login</button>
            </form>
        `;
    } else if (page === 'signup') {
        pageContainer.innerHTML = `
            <h1>Sign Up</h1>
            <form onsubmit="return handleSignUp()">
                <!-- Your Sign Up Form Fields Here -->
                <label for="signupFirstName">First Name:</label>
                <input type="text"id="signupFirstName" name="signupFirstName" required>

                <label for="signupLastName">Last Name:</label>
                <input type="text" id="signupLastName" name="signupLastName" required>

                <label for="signupEmail">Email:</label>
                <input type="email" id="signupEmail" name="signupEmail" required>
                <label for="signupPassword">Password:</label> <!-- Ensure correct ID for password field -->
                 <input type="password" id="signupPassword" name="signupPassword" required> <!-- Ensure correct ID for password field -->

                <button type="submit" id ="index.html" >Sign Up</button>
            </form>
        `;
  }
}