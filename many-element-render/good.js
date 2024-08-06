const btn = document.querySelector('#btn');

btn.addEventListener('click', () => {
  const datas = new Array(10000).fill(0).map((_, i) => i);
  renderChunks(datas);
});

/**
 * 分时渲染大量元素
 */
function renderChunks(data) {
  let index = 0;

  const  renderChunk=(deadline) =>{
    while (index < data.length && (deadline.timeRemaining() > 0 || deadline.didTimeout)) {
      const item = data[index];
      const div = document.createElement('div');
      div.textContent = item;
      document.body.appendChild(div);
      index++;
    }

    if (index < data.length) {
      requestIdleCallback(renderChunk);
    }
  }

  requestIdleCallback(renderChunk);
}
