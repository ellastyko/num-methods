'use strict';


window.onload = function(e) {
    let integer = document.querySelector('#int');
    let equation = document.querySelector('#equ');

    let xhr = new XMLHttpRequest();


    integer.onclick = (e) => {
        document.location.href = 'http://127.0.0.1:5000/definite_integral'
    }

    equation.onclick = (e) => {
        document.location.href = 'http://127.0.0.1:5000/differential_equation'
    }
}

