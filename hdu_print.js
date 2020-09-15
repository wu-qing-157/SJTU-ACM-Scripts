// Remove header and foot
top_rows = document.querySelectorAll('body > table > tbody > tr')
top_rows[0].remove()
top_rows[1].remove()
top_rows[top_rows.length - 1].remove()

// Remove bottom hrefs
document.querySelector('body > table > tbody > tr > td > center').remove()

// Remove "Author", "Source" and "Recommend", find "Sample Input" and "Sample Output"
titles = document.querySelectorAll('body > table > tbody > tr > td > div.panel_title')
contents = document.querySelectorAll('body > table > tbody > tr > td > div.panel_content')
bottoms = document.querySelectorAll('body > table > tbody > tr > td > div.panel_bottom')
brs = document.querySelectorAll('body > table > tbody > tr > td > br')
brs = Array.from(brs).slice(brs.length - titles.length)
for (i = 0; i < titles.length; i++) {
    if (['Author', 'Source', 'Recommend'].includes(titles[i].innerText)) {
        titles[i].remove()
        contents[i].remove()
        bottoms[i].remove()
        brs[i].remove()
    } else if (titles[i].innerText == 'Sample Input') {
        input_index = i
        brs[i].remove()
    } else if (titles[i].innerText == 'Sample Output') {
        output_index = i
        brs[i].remove()
    }
}

// Create new "Sample Input" and "Sample Output"
input = document.createElement('div')
input.appendChild(titles[input_index])
input.appendChild(contents[input_index])
input.appendChild(bottoms[input_index])
input.style.float = 'left'
input.style.width = '50%'
output = document.createElement('div')
output.appendChild(titles[output_index])
output.appendChild(contents[output_index])
output.appendChild(bottoms[output_index])
output.style.marginLeft = '50%'
tds = document.querySelectorAll('body > table > tbody > tr > td')
container = tds[tds.length - 1]
container.appendChild(input)
container.appendChild(output)

// Remove statistic and "Special Judge"
info = document.querySelector('body > table > tbody > tr > td > font > b > span')
info.innerText = info.innerText.split('\n')[0] + '\n'

// Enlarge font size
document.querySelectorAll('div.panel_title').forEach((d) => {
    d.style.fontSize = '27px'
    d.style.height = '57px'
})
document.querySelectorAll('div.panel_content,  div.panel_content > pre > div').forEach((d) => {
    d.style.fontSize = '21px'
})
document.querySelector('h1').style.fontSize = '3em'
document.querySelector('font > b > span').style.fontSize = '18px'

// Finally, print the result web page
window.print()
