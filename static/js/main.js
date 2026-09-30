document.addEventListener(
    "DOMContentLoaded",
    function () {

        console.log("Developwithvic JS loaded");


        const text = [
            "Developer.",
            "Server Engineer.",
            "Cybersecurity Specialist."
        ];


        let index = 0;
        let charIndex = 0;


        const typing = document.querySelector(".typing");


        if (!typing) {
            console.log("Typing element not found");
            return;
        }


        function type() {

            if (charIndex < text[index].length) {

                typing.textContent += text[index][charIndex];

                charIndex++;

                setTimeout(type, 100);

            } else {

                setTimeout(erase, 1500);

            }

        }


        function erase() {

            if (charIndex > 0) {

                typing.textContent =
                    text[index].substring(
                        0,
                        charIndex - 1
                    );

                charIndex--;

                setTimeout(erase, 50);

            } else {

                index++;

                if (index >= text.length) {
                    index = 0;
                }

                setTimeout(type, 500);

            }

        }


        type();


    }
);