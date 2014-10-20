package com.example.location;

import java.util.Timer;
import java.util.TimerTask;

import android.app.Service;
import android.content.ContentResolver;
import android.content.Intent;
import android.content.res.Configuration;
import android.os.IBinder;
import android.telephony.TelephonyManager;
import android.util.Log;

public class Locate_Data  extends Service{
	private String SIM_INFO;
	private int SIM_ID;
	@Override
	public IBinder onBind(Intent intent) {
		// TODO Auto-generated method stub
		Log.i("======", "��������");
		return null;
	}

	@Override
	public void onCreate() {
		// TODO Auto-generated method stub
		super.onCreate();
		//getSIM();
		Log.i("-------", "������~");
		
	}

	@Override
	public void onStart(Intent intent, int startId) {
		// TODO Auto-generated method stub
		super.onStart(intent, startId);
	}

	@Override
	public int onStartCommand(Intent intent, int flags, int startId) {
		// TODO Auto-generated method stub
		Log.i("~~~", "service started");
		getSIM();
	
		return super.onStartCommand(intent, flags, startId);
		
	}

	@Override
	public void onConfigurationChanged(Configuration newConfig) {
		// TODO Auto-generated method stub
		super.onConfigurationChanged(newConfig);
	}
	public void getSIM(){
	TelephonyManager telMge=(TelephonyManager)getSystemService(TELEPHONY_SERVICE);
	int simState=telMge.getSimState();//״̬
	String simSerialNumber=telMge.getSimSerialNumber();//����
	String simOperator=telMge.getSimOperator();//�����̺�
	String simOperatorName=telMge.getSimOperatorName();//����������
	String simCountryIso=	telMge.getSimCountryIso();//sim����
	int phonType=	telMge.getPhoneType();//�ֻ�����
	int netWorkType=	telMge.getNetworkType();//��������
	String netWorkOperatorName=	telMge.getNetworkOperatorName();//���繩Ӧ������
	String line1Number=	telMge.getLine1Number();//�ֻ�����
	boolean networkRoaming=	telMge.isNetworkRoaming();//����
	int dataState=	telMge.getDataState();//��������
	String deviceSoftwareVersion=	telMge.getDeviceSoftwareVersion();//Ӳ������汾
	String subScriberId=telMge.getSubscriberId();// �����û�ʶ���루��IMSI�����豸
	
	ContentResolver cv = this.getContentResolver();
		String tmpS = "";//�����Ƿ���
		tmpS = android.provider.Settings.System.getString(cv,android.provider.Settings.System.BLUETOOTH_ON);//WIFI�Ƿ���
		tmpS = android.provider.Settings.System.getString(cv,android.provider.Settings.System.WIFI_ON);
		//����ģʽ�Ƿ���
		tmpS = android.provider.Settings.System.getString(cv,android.provider.Settings.System.AIRPLANE_MODE_ON);
		//���������Ƿ���
		tmpS = android.provider.Settings.System.getString(cv,android.provider.Settings.System.DATA_ROAMING);
		SIM_INFO="{"+"\"SIM_ID\""+":"+(SIM_ID++)+","+"\"SIM_STATE\""+":"+simState+","+"\"SIM_SERIALNUMBER\""+":"+simSerialNumber
		+","+"\"SIM_OPERATER\""+":"+simOperator+","+"\"SIM_OPERATORNAME\""+":"+simOperatorName+","+"\"SIM_COUNTRYISO\""+":"+simCountryIso
		+"," +"\"PHONE_TYPE\""+":"+phonType+","+"\"NETWORK_TYPE\""+":"+netWorkType+","+"\"NETWORK_OPERATORNAME\""+":"+netWorkOperatorName+
			", "+"\"LINE1NUMBER\""+":"+line1Number+","+"\"NETWORKROAMING\""+":"+networkRoaming+","+"\"DATA_STATE\""+":"+dataState
			+"," +"\"DEVICESOFTWAREVERSION\""+":"+deviceSoftwareVersion+","+"\"SUB_SCRIBERID\""+":"+subScriberId+"}";
	Log.i("=======>", SIM_INFO);
	}
}
