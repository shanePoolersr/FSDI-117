//This is excecuted when the user press "Send Email"
document.getElementById("emailForm").addEventListener("submit", function (event) {
    event.preventDefault();

    const form = event.target; // This is the element that is getting the submit action (The form)

    //get values / The text
    const name = form.elements.name.value;
    const email = form.elements.email.value;
    const subject = form.elements.subject.value;
    const message = form.elements.message.value;

    //Now! Let's go and create yor EmailJS account: emailjs.com
    //Add the public  key - This is different for all of us!
    //Under account!
    emailjs.init("axzr vrdh unsc btjr");


    /*This is the object with the information you want to send in the email*/
    const params = {
        from_email: email,
        from_name: name,
        subject: subject,
        message: message
    };


    //verify if the subject is empty
    if (!subject) {
        const result = confirm("Subject is empty. Are you sure you want to send the email?");
        //This returns ok = True

        if (result === true) {
            sendEmail();
        } else {
            //Do not send the email
            //Note: You do not need this else, you can omit it.
        }
    } else {
        sendEmail();
    }


    function sendEmail() {
        // Here you are using the EmailJS library to send the request (the email)

        // The first param is your Service ID (You can find it in EMAIL SERVICES)
        // The second param is your template ID (You can find it in EMAIL TEMPLATES)

        emailjs.send("service_khs1pmd", "template_2bpw2sv", params).then(function(response){
            alert("Email was successfully sent!");
            form.reset(); //Clear the form
        }, function (error) {
            alert("Error sending email");
        });
    }
});