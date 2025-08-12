const term = document.getElementById('terminal') as HTMLDivElement;
let buffer = '';
const lines: string[] = JSON.parse(localStorage.getItem('lines') || '[]');
(window as any).lines = lines;

function render() {
  if (!term) return;
  term.innerHTML = lines.join('<br>') + '<br><span class="prompt">&gt;&gt;&gt; </span>' + buffer;
}

document.addEventListener('keydown', (e: KeyboardEvent) => {
  if (e.key.length === 1) {
    buffer += e.key;
  } else if (e.key === 'Backspace') {
    buffer = buffer.slice(0, -1);
  } else if (e.key === 'Enter') {
    lines.push('&gt;&gt;&gt; ' + buffer);
    localStorage.setItem('lines', JSON.stringify(lines));
    buffer = '';
  }
  render();
  e.preventDefault();
});

function login() {
  // Placeholder for Google OIDC login
  localStorage.setItem('auth', 'google');
}

async function loadGameModule(name: string, cls: string) {
  const mod = await import(`./${cls}.ts`);
  mod.startGame(name);
}

render();
(window as any).login = login;
(window as any).loadGameModule = loadGameModule;
