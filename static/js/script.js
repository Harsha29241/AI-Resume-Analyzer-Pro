document.addEventListener("DOMContentLoaded", function () {

    const scoreElement = document.getElementById("ats-score");

    if (!scoreElement) return;

    const score = parseInt(scoreElement.value);

    const ctx = document.getElementById("atsChart").getContext("2d");

    new Chart(ctx, {

        type: "doughnut",

        data: {

            labels: ["ATS Score", "Remaining"],

            datasets: [{

                data: [score, 100-score],

                backgroundColor: [

                    "#4CAF50",

                    "#E0E0E0"

                ]

            }]
        },

        options: {

            plugins: {

                legend: {

                    position: "bottom"

                }

            }

        }

    });

});