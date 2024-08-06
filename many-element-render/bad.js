const btn = document.querySelector('#btn')

const datas = new Array(500000).fill(0).map((_, i) => i)

btn.addEventListener('click', () => {
  datas.forEach(data => {
    const div = document.createElement('div')
    div.textContent = data
    document.body.appendChild(div)
  })
})
