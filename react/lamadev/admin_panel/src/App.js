import TopBar from './components/topbar/Topbar';
import Sidebar from './components/sidebar/Sidebar';

import './app.css';

function App() {
  return (
    <div>
      <TopBar />
      <div className="container">
        <Sidebar />
        <div className="others">
          other pages
        </div>
      </div>
    </div>
  );
}

export default App;
