package com.example.location;

import java.io.OutputStream;
import java.util.ArrayList;

import android.os.Bundle;
import android.app.Activity;
import android.support.v4.view.ViewPager;
import android.support.v4.view.ViewPager.OnPageChangeListener;
import android.view.LayoutInflater;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.Toast;
import android.os.Bundle;
import android.app.Activity;
import android.content.Intent;
import android.content.SharedPreferences;
import android.content.SharedPreferences.Editor;
import android.support.v4.view.ViewPager;
import android.support.v4.view.ViewPager.OnPageChangeListener;
import android.view.LayoutInflater;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.Toast;

public class InitGuide extends Activity {
	// 定义ViewPager对象
	private ViewPager viewPager;
	// 定义ViewPager适配器
	private ViewPagerAdapter vpAdapter;
	// 定义一个ArrayList来存放View
	private ArrayList<View> views;
	// 引导图片资源
	private static final int[] pics = { R.drawable.initguide1,
			R.drawable.initguide2, R.drawable.initguide3,
			R.drawable.initguide4, R.drawable.initguide5 };
	// 底部小点的图片
	private ImageView[] points;
	// 记录当前选中位置
	private int currentIndex;
	private Editor editor;
	private OutputStream os;
	private SharedPreferences preferences;
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.initguide_main);
		preferences=getSharedPreferences("com.example.location_mypreferences", MODE_PRIVATE);
		String strCity=preferences.getString("ditCityPref", "北京");
		if(preferences.getBoolean("firststart",true)){
		editor=preferences.edit();
		editor.putBoolean("firststart", false);
		editor.commit();
		initView();
		initData();
		}else{
			finish();
		startActivity(new Intent(InitGuide.this, MainActivity.class));
		}
	}

	/**
	 * 初始化组件
	 */
	private void initView() {
		// 实例化ArrayList对象
		views = new ArrayList<View>();
		// 实例化ViewPager
		viewPager = (ViewPager) findViewById(R.id.viewpager);
		// 实例化ViewPager适配器
		vpAdapter = new ViewPagerAdapter(views);
	}
	/**
	 * 初始化数据
	 */
	private void initData() {
		LayoutInflater inflater = getLayoutInflater();

		for (int i = 0; i < pics.length; i++) {
			View v = inflater.inflate(R.layout.item_view, null);
			ImageView image = (ImageView) v.findViewById(R.id.image);
			image.setImageResource(pics[i]);
			views.add(v);
		}

		// 设置数据
		viewPager.setAdapter(vpAdapter);
		// 设置监听
		viewPager.setOnPageChangeListener(new pageListener());

		// 初始化底部小点
		initPoint();
	}

	/**
	 * 初始化底部小点
	 */
	private void initPoint() {
		LinearLayout linearLayout = (LinearLayout) findViewById(R.id.ll);

		points = new ImageView[pics.length];

		// 循环取得小点图片
		for (int i = 0; i < pics.length; i++) {
			// 得到一个LinearLayout下面的每一个子元素
			points[i] = (ImageView) linearLayout.getChildAt(i);
			// 默认都设为灰色
			points[i].setEnabled(true);
			// 给每个小点设置监听
			points[i].setOnClickListener(new pointListener());
			// 设置位置tag，方便取出与当前位置对应
			points[i].setTag(i);
		}

		// 设置当面默认的位置
		currentIndex = 0;
		// 设置为白色，即选中状态
		points[currentIndex].setEnabled(false);
	}

	private class pageListener implements OnPageChangeListener {

		/**
		 * 当滑动状态改变时调用
		 */
		@Override
		public void onPageScrollStateChanged(int arg0) {
			// TODO Auto-generated method stub

		}

		/**
		 * 当当前页面被滑动时调用
		 */
		@Override
		public void onPageScrolled(int arg0, float arg1, int arg2) {
			// TODO Auto-generated method stub

		}

		/**
		 * 当新的页面被选中时调用
		 */
		@Override
		public void onPageSelected(int position) {
			// 设置底部小点选中状态
			setCurDot(position);
		}

	}

	private class pointListener implements OnClickListener {
		/**
		 * 通过点击事件来切换当前的页面
		 */
		@Override
		public void onClick(View v) {
			int position = (Integer) v.getTag();
			setCurView(position);
			setCurDot(position);
		}

	}

	/**
	 * 设置当前页面的位置
	 */
	private void setCurView(int position) {
		if (position < 0 || position >= pics.length) {
			return;
		}
		viewPager.setCurrentItem(position);
	}

	/**
	 * 设置当前的小点的位置
	 */
	private void setCurDot(int positon) {
		if (positon < 0 || positon > pics.length - 1 || currentIndex == positon) {
			return;
		}
		points[positon].setEnabled(false);
		points[currentIndex].setEnabled(true);
		currentIndex = positon;
	}

	public void Init(View v) {
		startActivity(new Intent(InitGuide.this, MainActivity.class));
		Toast.makeText(this, "欢迎使用", 1).show();

	}

}
