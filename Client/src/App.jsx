import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import {getApi} from "./api/tiendaVirtual.api";
import { useEffect } from "react";

const App = () => {
  useEffect(() => {
    async function loadApi() {
      const res = await getApi();
      console.log(res)
    }
    loadApi()
  }, []);

  return (
    <BrowserRouter>
    
      <Routes>
        <Route path='/' element={<Navigate to='' />} />
        {/* <Route path="" element={}/> */}
      </Routes>
    </BrowserRouter>
  );
};

export default App;
