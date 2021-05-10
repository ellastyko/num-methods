'use strict';


document.addEventListener('DOMContentLoaded', (e) => {

    let integral_submit = document.querySelector('#integral_submit');
    let tg = document.querySelector('.table-grafic');
    let result = document.querySelector('#result');
    var xhr = new XMLHttpRequest();


    integral_submit.onclick = (e) => {
        e.preventDefault()
        let data = {
            type: 'definite-integral',
            body: {
                example:   document.querySelector('#example').value,
                begin:      document.querySelector('#begin').value,
                end:        document.querySelector('#end').value,
                n:          document.querySelector('#n').value,
                method:     document.querySelector('#method').value,
                compare:    document.querySelector('#compare').checked
            }              
        }
        console.log(data)
        
        xhr.open('POST', 'http://127.0.0.1:5000/definite_integral');

        xhr.setRequestHeader('Content-type', 'application/json');

        xhr.onreadystatechange = function () {
            if(xhr.readyState === 4 && xhr.status === 200) {

                let response = JSON.parse((xhr.responseText))

                if (response.type === 'result') {

                    if (typeof(response.body) == 'object') {

                        result.hidden = true
                        let array = response.body
                        var data = [{
                            type: 'table',
                                header: {
                
                                    values: ['Left Rectagles', 'Right rectagles', 'Center rectagles', 
                                            'Trapezoidal', 'Simpson`s'],
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
                    else {
                        if (tg.children.length != 0) 
                            tg.removeChild(tg?.childNodes[0])
                        result.innerHTML = 'S = ' + response.body
                        result.hidden = false
                    }
                }
            }
        }
        xhr.send(JSON.stringify(data));          
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