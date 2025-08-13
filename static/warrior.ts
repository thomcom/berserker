export function startGame(name: string) {
  const lines = (window as any).lines as string[];
  lines.push(`Welcome ${name} the warrior!`);
}
