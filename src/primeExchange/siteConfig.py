def setSiteSpecificConfigValues():
#    from .settings import BASE_DIR
    configValues = {}
    configValues['clientID'] = 'gleneagles_lbn'
    configValues['thresholdProbability'] = 70.0
    configValues['predictable_service_codes'] = ['100','115','109','100','101','167','168','169']
    configValues['siteZipCode'] = 500035
# Data Quality Related Configuration
    configValues['NumericColumns']=['UHID','AdmissionNumber','PatientContact','BillingNumber','RegistrationNumber','PatientZIP','NumberOfUnitsOfService','ServiceAmount','FinalBillAmount',
        'FinalDiscountAmount','PaymentAmount','FinalBillingID','FinalEncounterID']
    configValues['NotNullColumns']=['PatientName','UHID','PatientGender','BillingNumber','ServiceCode','ServiceName','DoctorName','PaymentMode','UpdatedBy']
    configValues['FromDateFormat']="%d-%m-%Y"
    configValues['ToDateFormat']="%Y-%m-%d"
    configValues['ToBeReformattedDateTimeColumns']=['RegistrationDate','BillingDate','PatientDateOfBirth','PaymentDate','UpdatedOn','NextVisitDate']
    configValues['TobeValidateDateTimeColumns']=['RegistrationDate','BillingDate','PatientDateOfBirth','PaymentDate','UpdatedOn','NextVisitDate']
    configValues['TimeColumns']=['TimeOfBilling']
    configValues['Integers']=['PatientAnnualIncomeRange','FinalEncounterID','AdmissionNumber','RegistrationNumber','PatientZIP','PatientContact','NumberOfUnitsOfService','FinalBillingID']
    configValues['Dates']=['RegistrationDate','BillingDate','PatientDateOfBirth','PaymentDate','NextVisitDate']
    configValues['SmallIntegers']=['pd_distance','pd_patientGenderID','pd_hospitalLoadID','pd_weatherDescID','pd_weatherTempID','pd_weekDayID','pd_CCHolderID','pd_patientAge','pd_doctorID','pd_specializationID']
    configValues['Decimals']=['ServiceAmount','FinalBillAmount','FinalDiscountAmount','PaymentAmount']
# Peak Hours Related Configuration
    configValues['MorningFrom']=10
    configValues['MorningTo']=14
    configValues['EveningFrom']=15
    configValues['EveningTo']=18
    configValues['NightFrom']=16
    configValues['NightTo']=18
# Directories Specific to the site
#    configValues['historicalDataDir']=BASE_DIR+'/data/historyData/'
#    configValues['inProcessDataDir']=BASE_DIR+'/data/inProcessData/'
#    configValues['predictiveModelDir']=BASE_DIR+'/model/'
#    configValues['masterDataDir']=BASE_DIR+'/data/masterData/'
# URL Specific Information
    configValues['URL']='http://192.168.132.145:8000/primeProcessPredict/'
#    configValues['URL']='http://ec2-34-212-50-89.us-west-2.compute.amazonaws.com:8000/primeProcessPredict/'

    configValues['SMSGatewayURL']='http://boancomm.net/boansms/boansmsinterface.aspx?pid=49&uname=global&pwd=global08&mobileno='
# eAutomation support Contacts
    configValues['eAutomatonSupportContacts'] = [['Raja','9959047000']]
    configValues['PrimeSupportSMSGatewayURL']='http://boancomm.net/boansms/boansmsinterface.aspx?pid=49&uname=global&pwd=global08&mobileno='
    return configValues
