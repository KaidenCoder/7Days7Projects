import React from 'react'
import { NavLink } from 'react-router-dom'

const Navbar = () => {
    return (
        // <div style={{ textAlign: "center", justifyContent: "center" }}>
        //     <ul className="nav center mx-auto">
        //         {/* <li className="nav-item">
        //             <a className="nav-link active" href="/">30DaysChallenge</a>
        //         </li> */}
        //         <li className="nav-link"><NavLink exact to="/">30DaysChallenge</NavLink></li>
        //         <li className="nav-link"><NavLink exact to="/">60DaysChallenge</NavLink></li>
        //         <li className="nav-link"><NavLink exact to="/">About</NavLink></li>
        //     </ul>
        // </div>
        <nav className="navbar navbar-expand-lg navbar-light bg-light center">
            <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
                <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarNavAltMarkup">
                <div className="navbar-nav mx-auto">
                    <NavLink className="nav-link" exact to="/">30DaysChallenge</NavLink>
                    <NavLink className="nav-link" exact to="/sixty">60DaysChallenge</NavLink>
                    <NavLink className="nav-link" exact to="/about">About</NavLink>

                </div>
            </div>
        </nav>
    )
}

export default Navbar
