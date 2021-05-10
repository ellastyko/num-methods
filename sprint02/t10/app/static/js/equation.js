'use strict';
let array;
let enumerate;

document.addEventListener('DOMContentLoaded', (e) => {

    let equation_submit = document.querySelector('#equation_submit');
    let tg = document.querySelector('.table-grafic');
    let change_result = document.querySelector('#change-result');


    var xhr = new XMLHttpRequest();

    equation_submit.onclick = (e) => {
        e.preventDefault()
        let data = {
            type: 'differential-equation',
            body: {
                example:   document.querySelector('#example').value,
                begin:      document.querySelector('#begin').value,
                end:        document.querySelector('#end').value,
                n:          document.querySelector('#n').value,
                y0:          document.querySelector('#y0').value,
                method:     document.querySelector('#method').value
            }              
        }
        // console.log(data)
        xhr.open('POST', 'http://127.0.0.1:5000/differential_equation');
        xhr.setRequestHeader('Content-type', 'application/json');
        xhr.onreadystatechange = function () {
            if(xhr.readyState === 4 && xhr.status === 200) {
                
                let response = JSON.parse((xhr.responseText))               
                
                if (response.type === 'result') {
                    array = response.body.array
                    enumerate = response.body.enum
                    Plotly.newPlot( tg, [{
                                    x: enumerate,
                                    y: array }], {
                                    margin: { t: 0 } } );

                    change_result.innerHTML = "Table"
                    change_result.hidden = false   
                }                                        
            }
        }
        xhr.send(JSON.stringify(data));
    }

    change_result.onclick = (e) => {
        
        if (change_result.textContent == "Table") {
            change_result.innerHTML = "Graphic"
                     
            var data = [{
            type: 'table',
                header: {

                    values: enumerate.map((item, i, arr) => {
                        return item.toFixed(3)
                    }),
                    align: "center",
                    line: {width: 1, color: 'black'},
                    fill: {color: "grey"},
                    font: {family: "Arial", size: 12, color: "white"}
                },
                cells: {
                    values: array.map((item, i, arr) => {
                        return item.toFixed(3)
                    }),
                    align: "center",
                    line: {color: "black", width: 1},
                    font: {family: "Arial", size: 11, color: ["black"]}
                }
            }]
            Plotly.newPlot(
                tg,
                data
            );
        }
        else if (change_result.textContent == "Graphic") {

            change_result.innerHTML = "Table"
            Plotly.newPlot( tg, [{
                x: enumerate,
                y: array }], {
                margin: { t: 0 } } );
        }
    }
    
});




/* fetch("http://127.0.0.1:5000/", {
                
                // Adding method type
                method: "POST",
                
                // Adding body or contents to send
                body: JSON.stringify({
                    title: "solve",
                    body: data
                }),
                
                // Adding headers to the request
                headers: {
                    "Content-type": "application/json; charset=UTF-8"
                }
            })
            
            // Converting to JSON
            .then(response => JSON.stringify(response))
            
            // Displaying results to console
            .then(json => console.log(json))

            .catch((err) => {
                console.log(err)
            });*/