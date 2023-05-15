function demonio(checkboxElem) {

    const rotated = document.getElementById('gira');
    const rotated2 = document.getElementById('gira2');
    const rotated3 = document.getElementById('gira3');

    if (checkboxElem.checked) {
        rotated.style.transform = 'rotate(360deg)';
        rotated.style.transition ='1s ease';
        rotated2.style.transform = 'rotate(360deg)';
        rotated2.style.transition ='1s ease';
        rotated3.style.transform = 'rotate(360deg)';
        rotated3.style.transition ='1s ease';


    } else {

    }
  }