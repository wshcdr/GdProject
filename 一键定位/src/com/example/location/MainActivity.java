package com.example.location;

import com.baidu.location.BDLocation;
import com.baidu.location.BDLocationListener;
import com.baidu.location.LocationClient;
import com.baidu.location.LocationClientOption;
import com.baidu.location.LocationClientOption.LocationMode;
import com.baidu.mapapi.SDKInitializer;
import com.baidu.mapapi.map.BaiduMap;
import com.baidu.mapapi.map.BitmapDescriptor;
import com.baidu.mapapi.map.BitmapDescriptorFactory;
import com.baidu.mapapi.map.MapStatusUpdate;
import com.baidu.mapapi.map.MapStatusUpdateFactory;
import com.baidu.mapapi.map.MapView;
import com.baidu.mapapi.map.MyLocationConfiguration;
import com.baidu.mapapi.map.MyLocationData;
import com.baidu.mapapi.model.LatLng;
import com.baidu.mapapi.navi.BaiduMapNavigation;
import com.baidu.mapapi.search.core.SearchResult;
import com.baidu.mapapi.search.geocode.GeoCodeOption;
import com.baidu.mapapi.search.geocode.GeoCodeResult;
import com.baidu.mapapi.search.geocode.GeoCoder;
import com.baidu.mapapi.search.geocode.OnGetGeoCoderResultListener;
import com.baidu.mapapi.search.geocode.ReverseGeoCodeResult;
import com.baidu.navisdk.BNaviEngineManager.NaviEngineInitListener;
import com.baidu.navisdk.BaiduNaviManager;
import com.baidu.navisdk.BaiduNaviManager.OnStartNavigationListener;
import com.baidu.navisdk.comapi.routeplan.RoutePlanParams.NE_RoutePlan_Mode;

import android.support.v7.app.ActionBarActivity;
import android.support.v7.app.ActionBar;
import android.support.v4.app.Fragment;
import android.telephony.TelephonyManager;
import android.telephony.gsm.SmsManager;
import android.telephony.gsm.SmsMessage;
import android.app.Activity;
import android.app.PendingIntent;
import android.content.ContentResolver;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.location.Geocoder;
import android.media.ExifInterface;
import android.net.Uri;
import android.os.Bundle;
import android.os.Environment;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Toast;
import android.os.Build;

public class MainActivity extends ActionBarActivity implements OnGetGeoCoderResultListener {
	/*当前存在问题如下：
	 * 1、离线地图，地理路径规划 
	 * 2、在service中进行定位（间隔一段时间自动定位）
	 * 3、程序启动后自动开启定位服务，（测试功能有数据记录 将记录做成json格式完成上传）
	 * 4、程序某些功能可以在开机启动后自动运行，（数据记录和上传）
	 * 5、实时生效功能，当在设置中完成设置更改后在程序中能够马上得到应用更改和相应的反应
	 * 6、使用Alarm进行程序激活，和broadcast reciver一起使用
	 * 目前主要进行功能剥离，不同功能放在不同类中
	 * */
	MapView mMapView;
	BaiduMap mBaiduMap;
	public LocationClient mLocationClient = null;
	public MyLocationListener myListener = new MyLocationListener();
	public StringBuffer sb;
	public Boolean isFirstPoi = true;
	BitmapDescriptor mCurrentMarker;
	public MyLocationConfiguration.LocationMode currentMode;
	public Boolean mIsEngineInitSuccess=false;
	private SharedPreferences preferences;
	public Boolean isStateLiteOn;//是否开启卫星地图
	private String defCity,defDestination;//默认城市和详细地址
	private String mapZoomBy;//设置地图缩放级别
	private double LOCATE_LATITITUDE,LOCATE_LONGTITUDE;//当前定位位置的经纬度
	private String LOCATITON_NOW;//当前位置
	private String LOCATION_INFOMATION;
	private double DESTINATION_LATITUDE,DESTINATION_LONGTITUDE;
	private NaviEngineInitListener mNaviEngineInitListerner=new NaviEngineInitListener() {
		
		@Override
		public void engineInitSuccess() {
			// TODO Auto-generated method stub
			mIsEngineInitSuccess=true;
		}
		
		@Override
		public void engineInitStart() {
			// TODO Auto-generated method stub
			
		}
		
		@Override
		public void engineInitFail() {
			// TODO Auto-generated method stub
			
		}
	};
	private String getSdcardDir(){
		if(Environment.getExternalStorageState().equalsIgnoreCase(Environment.MEDIA_MOUNTED)){
			return Environment.getExternalStorageDirectory().toString();
		}
		return null;
	}
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
	SDKInitializer.initialize(getApplicationContext());
		BaiduNaviManager.getInstance().initEngine(
				this, getSdcardDir(),mNaviEngineInitListerner, "r8XZhyHuSN7bsfYbYtLIgrDE",null);
		setContentView(R.layout.activity_main);
		   if (savedInstanceState == null) {
	            getSupportFragmentManager().beginTransaction()
	                    .add(R.id.container, new PlaceholderFragment())
	                    .commit();
	        }
		   Intent intent_service=new Intent(this, Locate_Data.class);
		   startService(intent_service);//开启服务 service
		 //  Toast.makeText(this, "开启服务", 1).show();
		mMapView = (MapView) findViewById(R.id.bmapView);
		mBaiduMap = mMapView.getMap();
		mBaiduMap.setMyLocationEnabled(true);
		preferences=getSharedPreferences("com.example.location_preferences",MODE_PRIVATE);
		isStateLiteOn=preferences.getBoolean("statelite", false);
		String mapZoomBy=preferences.getString("mapzoomPref", "8");
	//	Toast.makeText(this, "返回的缩放级别为"+mapZoomBy,1).show();;
		if(isStateLiteOn){//设置卫星地图
			mBaiduMap.setMapType(BaiduMap.MAP_TYPE_SATELLITE);
		}else{
			mBaiduMap.setMapType(BaiduMap.MAP_TYPE_NORMAL);
		}
		//设置地图缩放级别,z注意类型间的转换
		mBaiduMap.setMapStatus(MapStatusUpdateFactory.zoomTo(Float.parseFloat(mapZoomBy)));
		mLocationClient = new LocationClient(getApplicationContext());
		// mLocationClient.registerLocationListener(myListener);
		
	}

	public void Locate(View v) {
		LocationClientOption localLocationClientOption = new LocationClientOption();
		localLocationClientOption
				.setLocationMode(LocationClientOption.LocationMode.Hight_Accuracy);
		localLocationClientOption.setCoorType("bd09ll");
		localLocationClientOption.setScanSpan(1000 * 60 * 30);
		localLocationClientOption.setIsNeedAddress(true);
		
		localLocationClientOption.setNeedDeviceDirect(true);
		currentMode = MyLocationConfiguration.LocationMode.NORMAL;
		mCurrentMarker = BitmapDescriptorFactory
				.fromResource(R.drawable.icon_geo);
		mLocationClient.registerLocationListener(myListener);
		mLocationClient.setLocOption(localLocationClientOption);
		mLocationClient.start();
		if ((mLocationClient != null) && (mLocationClient.isStarted())) {
			mLocationClient.requestLocation();
			while (isFirstPoi) {
				isFirstPoi = false;
			//	Log.i("地图状态信息--->", mBaiduMap.getMapStatus().toString());
				return;
			}
		}
		
	}

	public class MyLocationListener implements BDLocationListener {

		@Override
		public void onReceiveLocation(BDLocation locationInfo) {
			// TODO Auto-generated method stub
			if ((locationInfo == null || mMapView == null))
				return;
			MyLocationData myLocationData = new MyLocationData.Builder()
					.accuracy(locationInfo.getRadius())
					.latitude(locationInfo.getLatitude())
					.longitude(locationInfo.getLongitude()).build();
			mBaiduMap.setMyLocationData(myLocationData);
			if (isFirstPoi) {
				isFirstPoi = false;
				MapStatusUpdate localMapStatues = MapStatusUpdateFactory
						.newLatLng(new LatLng(locationInfo.getLatitude(),
								locationInfo.getLongitude()));
				mBaiduMap.animateMapStatus(localMapStatues);

			}
			sb = new StringBuffer(256);
			sb.append("定位时间（time）:");
			sb.append(locationInfo.getTime());
			sb.append(locationInfo.getLocType());
			sb.append("\n纬度 （latitude）: ");
			sb.append(locationInfo.getLatitude());
			sb.append("\n经度（longitude） : ");
			sb.append(locationInfo.getLongitude());
			sb.append("\n定位精度（radius） : ");
			sb.append(locationInfo.getRadius());
			if (locationInfo.getLocType() == 61) {
				sb.append("\nspeed : ");
				sb.append(locationInfo.getSpeed());
				sb.append("\nsatellite : ");
				sb.append(locationInfo.getSatelliteNumber());
			}
			/*获取当前经纬度和当前地理位置
			 * 
			 * */
			LOCATION_INFOMATION=sb.toString();
			LOCATE_LATITITUDE=locationInfo.getLatitude();
			LOCATE_LONGTITUDE=locationInfo.getLongitude();
			LOCATITON_NOW=locationInfo.getAddrStr();
			Log.i("--------", String.valueOf(LOCATE_LATITITUDE)+String.valueOf(LOCATE_LONGTITUDE)+LOCATITON_NOW);
			Toast.makeText(getBaseContext(), sb.toString(), 1).show();
			while (isFirstPoi) {
				//此处有问题，需要修改，--->初步推测是循环条件问题
				isFirstPoi = false;
				//Toast.makeText(getBaseContext(), sb.toString(), 1).show();
				
			}

		}

	

	}
	public void Send(View v){
	//	getSIM();
		
		preferences=getSharedPreferences("com.example.location_preferences",MODE_PRIVATE);
		String NUMBER_TO=preferences.getString("editNumPref", "13488463145");
		PendingIntent paIntent = PendingIntent.getBroadcast(this, 0, new Intent(), 0);
		SmsManager smsManager = SmsManager.getDefault();
		smsManager.sendTextMessage(NUMBER_TO, null, LOCATION_INFOMATION, paIntent,null);
		
	}
	public void RouteGuide(View v){
		/*
		 *进行导航，在导航之前需先获取当前所在位置即需进行先定位
		 *下一步进行在service中进行定位
		 * */
		/*此处需进行反编码处理，将地理位置转换为经纬度坐标
		 * 
		 * */
		GeoCoder mSearch = null;
		mSearch=GeoCoder.newInstance();
		preferences=getSharedPreferences("com.example.location_preferences",MODE_PRIVATE);
		String Destination=preferences.getString("ditCityPref", "广州");
		String destinationDetail=preferences.getString("editDesPref", "广州塔");
		mSearch.geocode(new GeoCodeOption().city(Destination).address(destinationDetail));
		mSearch.setOnGetGeoCodeResultListener(this);
		BaiduNaviManager.getInstance().launchNavigator(this,   
	          LOCATE_LATITITUDE, LOCATE_LONGTITUDE,LOCATITON_NOW,   
	          DESTINATION_LATITUDE, DESTINATION_LONGTITUDE,"目的地",  
	            NE_RoutePlan_Mode.ROUTE_PLAN_MOD_MIN_TIME,       //算路方式  
	            true,                                            //真实导航  
	            BaiduNaviManager.STRATEGY_FORCE_ONLINE_PRIORITY, //在离线策略  
	            new OnStartNavigationListener() {                //跳转监听  
	 
	                @Override  
	                public void onJumpToNavigator(Bundle configParams) {  
	                    Intent intent = new Intent(MainActivity.this, BNavigatorActivity.class);  
	                    intent.putExtras(configParams);  
	                    startActivity(intent);  
	                }  
	 
	                @Override  
	                public void onJumpToDownloader() {  
	                }  
	            });
		
	}
 @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();
        if (id == R.id.action_settings) {
           // Toast.makeText(getBaseContext(), "进行设置", 1).show();
            startActivityForResult(new Intent(this, ApprefenceActivity.class), 0);
         if(id==R.id.action_exit){
           	 System.exit(1);
            }
            return true;
        
        }
        return super.onOptionsItemSelected(item);
    }

    /**
     * A placeholder fragment containing a simple view.
     */
    public static class PlaceholderFragment extends Fragment {

        public PlaceholderFragment() {
        }

        @Override
        public View onCreateView(LayoutInflater inflater, ViewGroup container,
                Bundle savedInstanceState) {
            View rootView = inflater.inflate(R.layout.fragment_main, container, false);
            return rootView;
        }
        
    }
	@Override
	public void onGetGeoCodeResult(GeoCodeResult result) {
		// TODO Auto-generated method stub
		if (result == null || result.error != SearchResult.ERRORNO.NO_ERROR) {
			Toast.makeText(this, "抱歉，未能找到结果", Toast.LENGTH_LONG)
					.show();
			return;
		}
		String strInfo = String.format("纬度：%f 经度：%f",
				result.getLocation().latitude, result.getLocation().longitude);
		DESTINATION_LATITUDE=result.getLocation().latitude;
		DESTINATION_LONGTITUDE=result.getLocation().longitude;
		//Toast.makeText(this, strInfo, Toast.LENGTH_LONG).show();
	}
	@Override
	public void onGetReverseGeoCodeResult(ReverseGeoCodeResult arg0) {
		// TODO Auto-generated method stub
		
	}
    
	
}
