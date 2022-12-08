import streamlit as st
import streamlit_book as stb

st.markdown("""<style>
.button {
  border: none;
  color: white;
  padding: 16px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  transition-duration: 0.4s;
  cursor: pointer;
}

h1{
  text-align: center;
}

.button1 {
  background-color: white; 
  color: black; 
  border: 2px solid #990000;
  align-items: center;
  display: inline-block;
  display: block;     
  width: 200px;
}  

.margin-auto {    
  margin: 0 auto;
}

.button1:hover {
  background-color: #990000;
  color: white;
}


.center {
margin: 0;
position: absolute;
top: 150%;
left: 20%;
-ms-transform: translate(-50%, -50%);
transform: translate(-50%, -50%);
}


.center2 {
margin: 0;
position: absolute;
top: 150%;
left: 80%;
-ms-transform: translate(-50%, -50%);
transform: translate(-50%, -50%);
}

.button2 {
  background-color: white; 
  color: black; 
  border: 2px solid #990000;
  align-items: center;
  display: inline-block;
  display: block;     
  width: 200px;
}  

.button2:hover {
  background-color: #990000;
  color: white;
}

.center-image {
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 50%;
  height: 50%;
}


</style>
</head>
<body>
<img class="center-image" 
src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxAQDxESEBIWFhUWDRcYFhcYFRUVGhUVFxcYGB0YGhUZHSgiGBsnHRUWITUiJSkrLi4uGx8zODMtNygtLi4BCgoKDg0OGxAQGy4lICU2LS0vLS0vLS8tLS0uLS8tLSstLS0tLS0tLS0tLS0tLS0tLi8tLS0tLS0tLS8tLS0tLf/AABEIAMkA+wMBIgACEQEDEQH/xAAcAAEAAgMBAQEAAAAAAAAAAAAAAQUEBgcDAgj/xABKEAACAQIDBAYECAsHBAMAAAABAgADEQQSIQUGMVETIkFhcYEHMpGhQlJzgrGywdEUFjM0NUNTYnKS4RUjJKLC8PFjk8PSF3SD/8QAGwEBAAIDAQEAAAAAAAAAAAAAAAQFAgMGAQf/xAA6EQABAwMBBAgDBwMFAQAAAAABAAIRAwQhMRJBUXEFImGBkbHB8BMyoQYzQlKy0eEUI6IWU3KS8RX/2gAMAwEAAhEDEQA/AO4yJMiEUxEQiSJMiEUxEQiREQiREQiREQiREQiREQiREQiREQiREQiREQiiTIkwiREQiREQiSJMiEUxEQiSJMiEUxEQiRE8MTiFpoWc2UDUzwkASUAnAXvE1wb1Us1sjZedxf8Al/rL3D1ldQym4IuDI9C8oVyRScDGvvh2jC3VbepSgvESsbH7Tp0dGN2t6o1P9JUVd5X+DTA8ST9FpXbWputepn7XJB5qTpby0njinps96aFVsNCb+OsvaVrTABImczuXP1ryrtEA7MYjfz9wrVN5anainwuPvlhgtu0qhCsMhPPUHz++a1iqlMvdEKrp1b38dYxJV6h6JCAbALxN5k62pu3R6eixbeVWEnaBg+PaPc9i32VG823KWAwtTEVrkLYBRxdzoqjvJ9gueyZ2DVlpoG9YKAfG04X6W946mJxr4b1aOGqEAfHqZRmdvaQO657ZUPOyr6mNpZv/AMx47pQegw/R39T+8zW5dLmtfvyeU6JuXvxh9qB1RWp1EW7U2IPVvbMrD1hfTsI001E5du56P2cJVxbWUrcU1vm1GmZvg87C8sNy92a+Cx2CrF+s2Mq0WS1r08lWzXvqCEz28OU0Nq5iVKfbnZmIXYcVtGlSIFQ2JFxoTfzAmo7Uz1azOmNekptZF6Wy2UDsI42vw7ZtG2cF01IgesNV+7z+6adLmya2NoHOh0PmCuevq1RrtkgRqNfQjRWWBxmIRFpjFK1tAz0XZjc9rZteMsKWKxS16CValNlqVGUhaZUjLTdr3LHtUTXZbYPE9JWwV/WWtUB/7NSxm2tR1MA4dOG8CQcALG3uC4hpxpGTxAIyStskzDqYUly4qOt1AsCLC1+wgjtn1hKhKjNxDMptpcqxW9uy9rymDztbJHH6K5LcSD79hZMmRJmaxSIiESIiESRJkQimIiESRJkQimYVSu2cqigkAElmygXvYXAJJ05TMmPSwuV3bMxzW0J0FuU1vkwB36ad6zaBmR5+kLxZq916qWzdazMbLY81Hd/vUYe9SM2GJXscE/w2I+kiXc+SL6Ga61D4tJ9MuPWEcsdyzp1fh1GvDdPr5rQOmoKt6anOy2s2qppYkfGJ7L8JtG69Nlwy5u1iR4H/AGT5z3/sXD5s3RLfzt/Le0zndVFyQAPISDZWFSjUNSoW4BADRAzEk9pjlwwAFKurtlRgYwHjnXl78JlfGIw6VBZ1DDv+zlK193qJ4Fl7gQR7xM19o0ApZqqBVFyWYKAOZJ7Jp+8HpKw1EFcMOmf43q0x87i3kLd8vbf4zjFKfT9lUXDKQ+9A79f3Wwru5S7Wb3D7J8UNiPSqB6VQadjL2ciRNJ2N6TaqNkx1K4JuGRcrKDqL02PWXvBvbnOg7K25hcWt8PWV9NVBsw8UOo8xN1b+pp/Pp3ELTTZbVI2cEcwVYre2vGa/tHc3Z+IxH4RWw6tV0u12GYgWBZQcrEADiDwE2KeGJrogzOwUcybf8yCYAkqc2ZwtXxFE02KtxHvHOfexaFJsWHe5qLRbo9eqMxGY5eGawAvyzDtMzNo4lMQqml1rHiOI7rcZXrTFI53JXvv1j3LK341Nh22uBbxVvmrTLX4PDfPL0W3yor7ApOxa7C5vYWtf2SiXeesGJOUrfQW4DxE+dq714nKhwtKnfXMHJN+Fstio58ZttOmLd79lr9gnHWwPHRV9z0ZU2ZezaA4ZPhqr38XKXxn9o+6fWG2DSp1EqBmJRiRe1rlWXsHJjNMpb84xkLhaGVTY30IOnwTUuePYJNbfjGIAWWhYrfTrad9qhy+BtOlNpeEQXDxCoxWtAQQ36LpUwcAHCnOoU9K5sDm0Zi3G3fNCTfvFkZglIjS5CvbX50sNlb2Yt8RQp1qaBKrCxCsCQeDKSSCLyG/o6qDtSMTiRwDtImYg7sHkpbb6mRs5zG48vMkb8jsW9SZEmRFJSIiESIiESRJkQimIiESV+2yRha5Gh6FvoMsJgbc/Na/yLfVM2UfvG8x5rCr8juR8lzfA7QL9VmObx4/1md0h5n2zVWqW8Z61No1GUKTp28z4zrX2xJ6q4OlX6nWV5hNoFsTQVWNunW5udesPdOh7Z2kmFoVK9QMVRbkLYk3IGlyB285yvYLA4qh8un1hOg+kH9F4r5MfXWVPSdICpTb71Cv+hahNGo7fPotXxnpXpj8lhWP8VRU9yhp7bL3mqY2mXqplKsbKiVMuWwscx0J48pqOyaxp4WkyWDNVqXbKpYgZLdYi4tc8OcnEYqpU9dy3ixP0zF3RjK7C1vVEnMknBI0IAzHFTmdJPt6m0esY0gAZAOsk6HgrTaFU16VdMTVRA7oaaoRWdFU3I6pyZjYfC4k8pXUGoUPzal1h+tqWdvFVtkXyBPfMdFJIAFyTYAakk9gE2/Z25oyZ8TUy6XyqQLfxOdPZ7ZJFG3tGQ44O7uA0HYBrPEmSo7q9xdOkDI3+J15k6R4LW3x5qDLiFFZb8HuWF+OWoDmXyNu6Yb7Hw7ENQrNRcG4WpcgH92qguPNfObw26eEqg9BWII5MlQeYH3zVNq7Lq4apkqDjqrDgw5j7pspVKNUwwweGn0054Wp7a1IAvEjjr9dQvfC7V25hwcrNWQDiMuIHjmF2HnMB98ajt/iEbN29Yj/K3D2zzRipupIPMGx9olvsvaNarXo06j9IjVUUioFe4LAEdcG2kiXvRFvctIrMDozq5v6TqpVr0nWomKbiJ/4u8xgKNl7ap12Ip5gQt9be4gyyYk8ZqO6o/vqvh9s22fNOnrOlaXpo0RDQAdSdRnVdv0XcPuLZtWpqZ7NHEL5Jn1PluBn1KVWCqNtYnEUSr0WsrdVwbWDdh4dusqcVisVVt0hptYW1vwM2jH4Jno1T0bMq0ixtp6vW0JBA4TWMZtqlVRAqutqdvgsezgVReXbefU/stdmvZhr9WHZni2Jbz/L3LhOn7f4dwXN0cJjJzodNNx7ZXzRqVwCCEtbUAkcO6Xm6tV6mOwoqNYK4y3Zmta5CqLaXPgJSYfaFPKyniQNWFiLcvGX27eKWtjcGtNFBRlzZQbsF1LN98v6h6rsRrmW/l1469TunSCqimOs3M6Y635tOGkOxiTGoIXXZMiTOXXQJERCJERCJIkyIRTERCJPGvRV1ZHF1ZbEcweye0q9tbT/BkUhczM1h2DTiTNdWq2iw1HmAFkymajgxomV8fi3gv2Cewx+LWC/YJ7/vlR+NlT9mntMfjVU/Zp7TIn+oqH+67/JSP/iv/I3/ABVxT3fwisGWggIIIIB0I1BmH6Qf0Xivkx9dZ44HeVnqIrUwAxAuCbgk2vrxnr6Qf0Xivkx9dZNsr5l28Pa4uggZns4qLc2pt2kFoEg6R28FyrAfmlH5Wr/45M+cD+aUflqv+ie2GoNUdUXizWF9NZ1tsf7ZPa/9blzlwP7kdjP0NWxbjYUNXeo36tBl/ia4v7AfbMHebar4is6kno0cqq9mhtmI7SZse7Gy6mG6TpCvWy2yknhfjcDnK2ruk7MzdKouxPqk8TeRW1qX9Q6o47gAfP32rc5j/gtY0byStaoVmpsHRirA6EaETddouMZs3pWHXClvBlNmt3EA+0StO57/ALZf5T98ucHsxqeDahmBYq4B1A617fTFzWpPLHNOQR4eGmiW9N7dprhgg+K5/M7YX53h/l1+sJO09k1cPl6TL1ibZTfhbmBznzsVrYmgeVZfpEnOe00y5pkQVGY0io0HWR5qu3U/LVfD/VNsmNsDdyph3ql2VldLC17ghr9olkmCcnXSfLvtHSdcXxq0esCAMdgX0LogGjainUEEF2va4lY0usLjjlGSlTFtL9/gBMZMAvaSfdPenTCiyi0i2NjVpO2qkQd2/wB96l1nseIhYW8eJxJw9UiqE6o1F10vY9hPAmaji6dOmiCiQxya2fMCf5Fyju18Zv64CniT0NVcyPowuRcceI1HCew9HWy/2B/7tX/2nadE3dO3puBB1nEcAMyuX6YtTVqN2YGO3iTu+q5xRsVJZrNYWHG57dZcbAVFxuDNNySXXPoVyk3BW/whabkno+2avCiR4Vqo/wBUytn7oYKhVWrTptnU3UtVquAeF8rMReWT+kqZDvmzOOrGWxHGJzrMk52YaKtli8EfLiM5n5p34ndpEAb8m/kxEpVapERCJERCJIkyIRTERCJNZ309Sj/E30CbNKLefAvVROjFypNx22I7PZIPSbHPtXtaJMeoKlWTg2u0nT+FrmwdcVSv8b7DLneLZ2HVS4IR7XCjg5/h7PHhKmjsvFowZabAg6HlMbFYat0gFRWzsRbNxYk2GvbOZp1DRtnUn0SSTIJBAEgARvmeXNXTmCpWD21AIGgIz/HvtTZX5ej8sn1hNk9IP6LxXyY+usqtmbIritTY0yoFRSSbaAG8tfSD+i8V8mPrrLz7OUn0522kdYaiOCrOmKjXjqkHB0XJ8B+aUflqv0JLDYh/xNH5USv2f+a0vlan0JLDY5/xFL5QTv7f7h3Op+t6424++HKn+hi6DnjPMfPK3eLapw2Haoou1wFBva5PE90rBTkwFJ+IrrPGeaXunvPWxFY0qwU9QsrKLWtbQjlrNszzJ1LZMFeCoqPfRrrR/ib6FlDsf84o/LL9Il1ve1xS8W+yUux/zij8sv0iWDMWp5O9VH1uG8x5hWuxN5hWujoQ68SLZTra/MeEs/7QPxRNG3U/LVfD7Zts+b/aGs+1vTSonZbAO7eO0HuXfdEk17VtSpkmfoSB5LJbaDdir754PtWqPgqPIn7Y6NuR9hnxKQ9IXO9/l+ys2sZ+ULf9mYelkSoi+tTBBuSdR38JYyj3Tr5sPl+IxHkdR9JHlLydta1BVotqN3gH9/quVuGltVzSdD/4kRE3rSokyJMIkREIkREIkiTIhFMREIkiTIhFMxq+FV8pYaq4YHtBBvMfGY0A5VPZqQfdKzA7YztUAV1yPa7fC0B8uPA68Js+A57SYwtZrtY7XK2SUG/NEvs3FgdmHLeSWY+5ZZUtoobA6H3e2ZNVAylWFwVII5g6ETwEscHHcvZDwQCuD7N1wq/u1mv85Vt9B9kysLVyVEb4rg+QM8sbgTs/GVcPVB6N/VbmlzlfvtqD86fdWkVNj/S3MHtE6O1e3rU+MuHa1xk94cSDwBbOqpLqmcVOTT2FogeLQCO2RuW9CpfhMLbrp+C1ukAKikxseYGnvtKrY+1QAKdQ8PVbu5GXWaaXUix0FafiLVfR6yf32gzjL1u3Kb6eFxNzzzGBA4CYuP2itIc2tov38hBaXuwhqKu3orguij4Kkn51vu98r9lG1emTwU5j3BOsfdeY9aqWYsxuSbmfG06/QUsv6yoLEfEQ668i3LlfnN9fqUfhDVwIHfqeQBk+GpAOduC6rt7mwT3HA5nQeOgKxd2dpYWg9Wpi63RrYWABZnNySFUAnTTs7Z9bU9KLXybNw6oL26WsM7nwUGy+ZPgJomNrCrUJ4qui9/MycKt6g7gT9g+mUdxY29W6dcOEkwM6AAR/OqvberVZbtpTAHqSVs675bZvc40+HRUSPZkmdT392nlOZ6DHsY0Bf3MBNcn12ef0f8z11rQdqxvgPSFkHuGhXc/RdtOvisC1XEuHqfhLrcKEGUBSAFHK5m5zUPRXgzS2VRLCxqM9TyZiFPmoU+c2+RHNa0kNEBZTKRETxFEmRJhEiIhEiIhEkSZEIpiIhEmFtKjUenlpkAk63JGnkPCZsietMGQsXN2gQte/savzX+Y/+sxsHsusWrAFNK9jqeORD9om1zBwWCFNqrBnbpKuchjcKbAWXTQWAkkXRAMxPLtUY2jMRPiqv+xq/Nf5j90usGrLTUPa4Wxt3TIiaX1XPEFbadBtMyJWvb3btUsfRyt1ai3NOpb1TyPNTpcefZOS1umwVT8HxlM2HqtyHxkbgyd30HSd7lXt3Z+Gr0SuKVSg7ToVPC6txU+E2UrkUxFT5RmZgtPEHdwO4gkaEhH0S4yzU4jUOHAjf6HIggFcg6MFcyEMvMcR3MOKnxnvg9o1KWgN15H7OUstr+j7E0D0uAqGotrhcwV7cePquPZ4Ga420ijlMVQZXHE5ejPmh0PjpLmldl4g9ccRAd3tMDvacnRiq6tq2ddg8HSW9zgD4O0GryrrE7bdhZBl7+J8uUr0R3JtcniT9pJ4ecxKu1cOvqqah/esij2Ek+6WeA3d2ltC3V6Gjfi4KJbmF9Zz3n2iZuudhvUbA/M6QP8Arh55HYx+LcsGWonrOk8G5Pe75RzBdyWDiNoU6RtStUq3sCB1VPZYfDb3eM0vbWNdnqU9cwciqx45gbFfG9wZ3Btg4TYuCr4sjpa1OiStRwPyh6qqi8EuxA568Z+fiSbkm5JuSeJJ1JPeTIQrhxJbJ3Fx1PYB+EDgNdTJkmxZQgCQABkAacyd57fDGBAFpkbMW4ZuZsPAf8zErtYeMs8GmWmo7r+3Wayt695lbOwLYivRoJ61SoqA8sx1PkDfymMBczf/AEPbL6bG1MQw6tCn1flKl1FvBQ/8wmD3bIJXoXYsLQWnTSmgsqIFUclUWA9gntESvWxIiIRRJkSYRIiIRIiIRJEmRCKYiIRJEmRCKZynejfnG4bGVqNPo8qFbZlYnVFbUhh2kzq04XvhhHrbWxCILksngBkTUnsEnWFNr3kOE49Qol48tYCDGfRZ1D0ibRd1RFplmcKoCPqzEAD1u0mWm8G8u2cDk6daIDg5SodhccQevodRKWru70aU3w7EVqbBw3xmU3Gh0FiNPfMTbW1cbtHL05VRSuFXLkBfgQQSTfS1+A9ssf6ZrnjZaI38VWi+aKbnOeQdy7BuvjXxGDo1qlsz0lY2va5AOl+yZm0gDRqX/ZmVO56suzcOAOsMOuh01CjQnsmeErVEAqBFBAz2JJPNbWst/E/bOdu9XsA12t2OHvkr+2/C+cCN/vgrBQBoJi7Q2dRxC5a9JKi8nUNbwvwPhMyJnocLGFTbN3ZwOGbNRw6K1/WIzMPBmuR5S5iJ6XFxkmV4AAIC5v6dHcbMpBfVbHIH7wEqMP8AMqnyE4RP0j6U9n9PsfFgcUQVR/8Akwc/5Qw85+bpNtz1Fi5XW527T7Ux9PDg5UCl6rDitJSAbfvEkKPG/ZLLerYrYHGVqBFlDXp8daTG6m546aHvBlp6D62Xa7L8fAVB5h6TfQGnUPSHuqNoYa9MDp6QJpnhmHbTJ77acjbvmL6kVIOiAYXB1Np0f0ObaFKvVwbkWq9emebquov3oAfmnnOcMpBIIIINiCLEEaEEdhnrg8U9J0q0zZ6bhlPIg39l/pM2PbtCF4DC/UUSt2BtVMZhqWIp8HS5HxWGjKe8MCPKWUr4hbEiIhFEmRJhEiIhEiIhEkSZEIpiIhEkSZEIpmv1N2aLValXg9QgsQeNgFHZwsJsETNlRzMtMLXUpMqCHiQqH8WaPf7f6THr7m4Zzc3v3H+k2aJtF3XGQ8rSbG2OtMeAWJs/CCjSWmvBRYeAEy4iaCSTJUlrQ0QEiIni9SIiEXliKK1EZHF1ZCrDmCLEewz8m4/Bth61Wi/rUqz0z3lGK387Xn63n559Mey+g2tUcDq16SVRyzAZGHtQN86SbYwSFi5V/ouxPR7ZwR7DUdD8+k6j/MVn6Wn5O2HiugxeGrXt0eLpOT+6rqT7gZ+sYuRkFGrlHpX3P9bH4df/ALCgeXSgfW9vMzl4Np+pHQEEEXBFiD2icK9Iu6BwFbpKK/4ao3V/6TcejPdxIPLTs19o1PwlCFc+h7b3R1nwTnq1bvSv2OB1l81F/mHnOvz8u4LEvSqJUpmzo4dDyZTfzGn+7z9Ibv7UTGYWliKfCol7fFbgy+TAjymFdkHaRqsoiJoWSiTIkwiREQiREQiSJMiEUxEQiSJMiEUxEQiREQiREQiREQiREQiTmHp22X0mDoYkDWjXysf+nWsPrrT9s6fKrefZYxmCxOHP6ygyqeT2up8mAPlM6btlwK8Oi/KrrcEcwZ+rt38Z+EYPDVh+swtN/wCZAftn5vwG62MqkAYd1+WvTt8z1vcZ+hNysBUw2z8NRqsrMlK11BAsSSoAPJSB5TdXqMdhpBIWXw3tG04EAq9mFtTZ9PE0Xo1lzI62YfaD2EGxB7CJmxIy8X5823ubicLizQVS4OtOpaylL8WPAMOBHPhxE6h6OsF+C0GoMxLNUz6nS5ABCr8EdWbDtqsq0spFy2gH2+Wkr9j4Qs4c6Kp9p5TCrcVHPDR3/wAqXSo0/gue7Xcf28lsUREzURRJkSYRIiIRIiIRJEmRCKYiIRJEmRCKYiIRIiIRIiIRIiIRIiIRJh47GrSGupPAf74CZkrsXs0VXDMxAC2sPE9vnMX7UdXVbKQZtdfRUOIqmpULZQC1tB22FvPhNj2YGFJQwsQO3lfT3T1oYVKfqqB39vtnvNdOkWmSVur1w9oa0QAkRE3KKsDaOB6bJrax18Dx89BMulTCqFUWAGk9ImIaJlZF7i0N3BIiJksVEmRJhEiIhEiIhEkSZEIpiIhEkSZEIpiIhEiIhEiIhEiIhEiIhEiIhEiIhEiIhEiIhEiIhFEmRJhEiIhEiIhF/9k=">
<h1>Anti-spam and anti-phishing solution</h1>

<p style="text-align: justify;">
The best way to keep your corporate email protected is to invest in email protection
solutions. Here at Gatefy, we have 2 email security solutions that will help your
company</p>

<h4>1. Gatefy Email Security </h4>

<p style="text-align: justify;"> It is a solution that protects your company against different types
of email threats, such as spam, phishing, ransomware, viruses, BEC (Business Email
Compromise), and social engineering.
</p>


<h4>2. Gatefy Anti-Fraud Protection </h4>
<p style="text-align: justify;">It is a DMARC-based solution that protects your
company’s domain. It prevents criminals from using your name and brand in spam,
phishing, and BEC scams, for example. In addition, the solution also improves the
delivery capacity of your emails, as in cases of email marketing, for example</p>


</body>

""", unsafe_allow_html=True)