/**
 * Register Page
 * @version 1
 * @author [Kaijian Xie] (https://git.shefcompsci.org.uk/acp22kx)
 *
 */

/* Module Imports
React library Components */
import React from 'react';
import {FcGoogle} from "react-icons/fc";

/* Local imports */
import './Register.css';
import {loginSubmit} from "../fragments/Login";
import { Notify } from '../fragments/Notify';

const registerOnclick = (event) => {
    event.preventDefault();

    /* Check if input valid */
    if (document.getElementById("firstNameInput").value === "") {
        Notify.error("First name can not be empty");
        return;
    }
    if (document.getElementById("passwordInput").value !== document.getElementById("confirmPasswordInput").value) {
        Notify.error("Passwords are not matched. ");
        return;
    }
    const myRequest = new Request("/auth/register", {
        credentials: "include",
        headers: new Headers({"Content-Type": "application/json"}),
        method: "POST",
        body: JSON.stringify({
            email: document.getElementById("emailInput").value,
            password: document.getElementById("passwordInput").value,
            first_name: document.getElementById("firstNameInput").value,
            last_name: document.getElementById("lastNameInput").value,
            phone_no:document.getElementById("phoneNumberInput").value,
        })
    });
    /* Send data to backend */
    fetch(myRequest).then((response) => {
        if (response.status === 200) {
            Notify.success('Registration successful!')
            return response.json()
        } else {
            Notify.error("Register failed. " + response.statusText)
        }
    }).then((data) => {
        if (data['response'] === "success"){
            loginSubmit(document.getElementById("emailInput").value, document.getElementById("passwordInput").value).then((data) => {
                if (data['response'] === "success"){
                    window.location.href = "/"
                } else {
                    Notify.error("Auto login failed! Please login again. ERROR_MESSAGE: " + data['message'])
                }
            })
        } else {
            Notify.error("Register failed. Please try again. ERROR_MESSAGE: " + data['message'])
        }
    })
};

export default function Register() {
    return (
        <div className={"flex justify-center items-center bg-gray-50 w-full h-full overflow-auto"}>
            <div className={"items-center grid grid-col-7 w-full p-8 md:w-1/2 bg-[#f3f9f7] rounded-2xl "}>
                <span
                    className={"justify-center flex w-full mt-2 md:mt-12 text-[#237759] font-bold text-3xl md:text-4xl lg:text-5xl"}>Create Account</span>
                <div className={"w-full lg:w-3/5 mx-auto my-auto"}>
                    <form onSubmit={registerOnclick}>
                        <div className={"md:grid md:grid-cols-2 gap-x-4 mt-6 mb-3"}>
                            <div>
                                <label className={"text-left block mb-2 text-xl font-medium text-gray-900 "}>*
                                    First Name</label>
                                <input
                                    className={"block w-full p-2 text-gray-900 border border-[#509E82] border-2 rounded-lg bg-gray-50 sm:text-md focus:outline-0"}
                                    type="text"
                                    id={"firstNameInput"}
                                    required
                                ></input>
                            </div>
                            <br className={"block md:hidden"}/>
                            <div>
                                <label
                                    className={" text-left block mb-2 text-xl font-medium text-gray-900 "}>*
                                    Last Name</label>
                                <input
                                    className={" block w-full p-2 text-gray-900 border border-[#509E82] border-2 rounded-lg bg-gray-50 sm:text-md focus:outline-0"}
                                    type="text"
                                    id={"lastNameInput"}
                                    required
                                ></input>
                            </div>
                        </div>
                        <div className={"flex flex-col mt-3 w-full"}>
                            <label className={"text-left block mb-2 text-xl font-medium text-gray-900 "}>*
                                Password</label>
                            <input
                                className={"block w-full p-2 text-gray-900 border border-[#509E82] border-2 rounded-lg bg-gray-50 sm:text-md focus:outline-0"}
                                type="password"
                                required
                                id={"passwordInput"}></input>
                        </div>
                        <div className={"flex flex-col mt-3 w-full"}>
                            <label className={"text-left block mb-2 text-xl font-medium text-gray-900 "}>*
                                Confirm Password</label>
                            <input
                                className={"block w-full p-2 text-gray-900 border border-[#509E82] border-2 rounded-lg bg-gray-50 sm:text-md focus:outline-0"}
                                required
                                type="password"
                                id={"confirmPasswordInput"}></input>
                        </div>
                        <div className={"flex flex-col mt-3 w-full"}>
                            <label className={"text-left block mb-2 text-xl font-medium text-gray-900 "}>*
                                Email</label>
                            <input
                                className={"block w-full p-2 text-gray-900 border border-[#509E82] border-2 rounded-lg bg-gray-50 sm:text-md focus:outline-0"}
                                required
                                type="text"
                                id={"emailInput"}></input>
                        </div>
                        <div className={"flex flex-col mt-3 w-full"}>
                            <label className={"text-left block mb-2 text-xl font-medium text-gray-900 "}>*
                                Phone Number</label>
                            <input
                                className={"block w-full p-2 text-gray-900 border border-[#509E82] border-2 rounded-lg bg-gray-50 sm:text-md focus:outline-0"}
                                required
                                type="text"
                                id={"phoneNumberInput"}
                            ></input>
                        </div>
                        <button type='submit' className='w-full'>
                            <div
                                className={"my-6 text-white flex bg-[#509E82] mx-auto h-full justify-center w-full text-lg p-2 items-center font-medium cursor-pointer rounded-lg hover:bg-[#4E8E77]"}>
                                    <span className="register">Continue</span>
                            </div>
                        </button>
                        <div
                            className={"mt-4 mb-6 text-black flex border border-2 border-[#509E82] bg-white mx-auto h-full justify-center w-full text-md p-2 items-center font-normal cursor-pointer rounded-lg hover:bg-gray-100"}>
                            <span className="g-register">Continue with Google </span>
                            <div className={"ml-2 "}><FcGoogle size={30}/></div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    );
}
