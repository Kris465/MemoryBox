// App.js
// 1. Объявляем дочерний компонент. Параметр {value} — это props.
function Square({ value }) {
  // 2. Возвращаем разметку, используя полученное значение.
  return <button className="square">{value}</button>;
}

// 3. Объявляем родительский компонент Board.
export default function Board() {
  return (
    <>
      <div className="board-row">
        {/* 4. 9 раз используем Square, каждый раз с разным prop 'value' */}
        <Square value="1" />
        <Square value="2" />
        <Square value="3" />
        {/* ... и так для остальных рядов */}
      </div>
      <div className="board-row">
        <Square value="4" />
        <Square value="5" />
        <Square value="6" />
      </div>
      <div className="board-row">
        <Square value="7" />
        <Square value="8" />
        <Square value="9" />
      </div>
    </>
  );
}