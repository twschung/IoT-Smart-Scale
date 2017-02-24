package com.example.selenatan.iotsmartscale;

public class user {
    public int id;
    public String username, password, email, firstName, lastName, dob, gender, height, weight, targetWeight, targetIntake;

    public user (int Id, String Username, String Password, String Email, String FirstName, String LastName, String DOB, String Gender, String Height, String Weight, String TargetWeight, String TargetIntake){
        this.id = Id;
        this.username = Username;
        this.password = Password;
        this.email = Email;
        this.firstName = FirstName;
        this.lastName = LastName;
        this.dob = DOB;
        this.gender = Gender;
        this.height = Height;
        this.weight = Weight;
        this.targetWeight = TargetWeight;
        this.targetIntake = TargetIntake;
    }

    public user (String Username, String Password){
        this(-1,Username,Password,"","","","","","","","","");
    }



}
